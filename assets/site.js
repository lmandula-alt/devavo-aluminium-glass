(function(){
  var WHATSAPP = '27790340115';
  var EMAIL = 'luthando@devavo.co.za';

  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

  // ---------- mobile menu ----------
  var toggle = document.getElementById('menuToggle');
  var nav = document.getElementById('primaryNav');
  if (toggle && nav) {
    toggle.addEventListener('click', function(){
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // ---------- gallery filters ----------
  Array.prototype.forEach.call(document.querySelectorAll('[data-gallery]'), function(wrap){
    var buttons = wrap.querySelectorAll('.filters button');
    var items = wrap.querySelectorAll('.gallery figure');
    Array.prototype.forEach.call(buttons, function(btn){
      btn.addEventListener('click', function(){
        var f = btn.getAttribute('data-filter');
        Array.prototype.forEach.call(buttons, function(b){ b.setAttribute('aria-pressed', b === btn ? 'true' : 'false'); });
        Array.prototype.forEach.call(items, function(it){
          it.hidden = !(f === 'all' || it.getAttribute('data-cat') === f);
        });
      });
    });
  });

  // ---------- lightbox ----------
  var lb = document.getElementById('lightbox');
  if (lb) {
    var lbImg = lb.querySelector('img'), lbCap = lb.querySelector('.cap');
    var list = [], pos = 0;
    function show(i){
      pos = (i + list.length) % list.length;
      var fig = list[pos], img = fig.querySelector('img');
      lbImg.src = img.getAttribute('data-full') || img.src;
      lbImg.alt = img.alt;
      lbCap.textContent = fig.querySelector('figcaption') ? fig.querySelector('figcaption').textContent : img.alt;
    }
    function open(fig){
      list = Array.prototype.filter.call(fig.parentNode.querySelectorAll('figure'), function(f){ return !f.hidden; });
      show(list.indexOf(fig));
      lb.classList.add('open');
      document.body.style.overflow = 'hidden';
      lb.querySelector('.x').focus();
    }
    function close(){ lb.classList.remove('open'); document.body.style.overflow = ''; }
    Array.prototype.forEach.call(document.querySelectorAll('.gallery figure'), function(fig){
      fig.tabIndex = 0;
      fig.addEventListener('click', function(){ open(fig); });
      fig.addEventListener('keydown', function(e){ if (e.key === 'Enter') open(fig); });
    });
    lb.querySelector('.x').addEventListener('click', close);
    lb.querySelector('.prev').addEventListener('click', function(){ show(pos - 1); });
    lb.querySelector('.next').addEventListener('click', function(){ show(pos + 1); });
    lb.addEventListener('click', function(e){ if (e.target === lb) close(); });
    document.addEventListener('keydown', function(e){
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') show(pos - 1);
      if (e.key === 'ArrowRight') show(pos + 1);
    });
  }

  // ---------- quote form: Netlify Forms, with WhatsApp / email fallback ----------
  Array.prototype.forEach.call(document.querySelectorAll('form.quote'), function(form){
    var success = form.querySelector('.form-success');
    form.addEventListener('submit', function(e){
      e.preventDefault();
      var v = function(n){ var el = form.elements[n]; return el ? el.value.trim() : ''; };
      var body = 'Name: ' + v('name') + '\nPhone: ' + v('phone') + '\nEmail: ' + v('email') +
        '\nDivision: ' + v('division') + '\nArea: ' + v('area') + '\n\nProject details:\n' + v('message');
      var whatsapp = 'https://wa.me/' + WHATSAPP + '?text=' + encodeURIComponent('Hi Devavo, I would like a quote.\n\n' + body);
      var mailto = 'mailto:' + EMAIL + '?subject=' + encodeURIComponent('Quote request: ' + v('division')) + '&body=' + encodeURIComponent(body);
      var button = form.querySelector('button[type="submit"]');
      var label = button.innerHTML;
      button.disabled = true;
      button.textContent = 'Sending...';

      fetch('/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams(new FormData(form)).toString()
      }).then(function(r){ return r.ok; }, function(){ return false; }).then(function(sent){
        success.textContent = sent
          ? 'Thanks, ' + v('name') + '. Your quote request has reached us and we will be in touch. Want a faster reply? '
          : 'Your request could not be sent from this page. Please send it to us on WhatsApp or by email: ';
        var wa = document.createElement('a');
        wa.href = whatsapp; wa.target = '_blank'; wa.rel = 'noopener';
        wa.textContent = sent ? 'Send it on WhatsApp too' : 'Send on WhatsApp';
        success.appendChild(wa);
        if (!sent) {
          success.appendChild(document.createTextNode(' or '));
          var em = document.createElement('a');
          em.href = mailto; em.textContent = 'send by email';
          success.appendChild(em);
        }
        success.classList.add('show');
        if (sent) form.reset();
        button.disabled = false;
        button.innerHTML = label;
      });
    });
  });
})();

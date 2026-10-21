(function(){
  var WHATSAPP = '27790340115';
  var EMAIL = 'luthando@devavo.co.za';
  var PHONE = '079 034 0115';

  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

  // ---------- open / closed status (Mon-Fri 08:00-16:00, South African time) ----------
  (function(){
    var els = document.querySelectorAll('[data-open-status]');
    if (!els.length) return;
    var parts = {};
    try {
      new Intl.DateTimeFormat('en-GB', { timeZone: 'Africa/Johannesburg', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false })
        .formatToParts(new Date()).forEach(function(p){ parts[p.type] = p.value; });
    } catch (e) { return; }
    var mins = parseInt(parts.hour, 10) % 24 * 60 + parseInt(parts.minute, 10);
    var weekend = parts.weekday === 'Sat' || parts.weekday === 'Sun';
    var open = !weekend && mins >= 480 && mins < 960;
    var label = open ? 'Open now' : weekend ? 'Weekend' : 'Closed now';
    var detail = open ? 'call ' + PHONE : 'call or WhatsApp ' + PHONE;
    Array.prototype.forEach.call(els, function(el){
      el.classList.add(open ? 'is-open' : 'is-closed');
      var span = el.querySelector('span');
      span.textContent = label;
      var more = document.createElement('span');
      more.className = 'tb-long';
      more.textContent = ' · ' + detail;
      span.appendChild(more);
    });
  })();

  // ---------- photo & video protection: no right-click save, drag-out or long-press save ----------
  var PROTECTED = 'img, video, .gallery figure, .mosaic a, .page-hero, .lightbox';
  document.addEventListener('contextmenu', function(e){
    if (e.target.closest && e.target.closest(PROTECTED)) e.preventDefault();
  });
  document.addEventListener('dragstart', function(e){
    if (e.target.tagName === 'IMG' || e.target.tagName === 'VIDEO') e.preventDefault();
  });

  // ---------- cookie consent, then Google Analytics / Meta Pixel ----------
  (function(){
    var cfg = window.DEVAVO_TRACKING;
    var KEY = 'devavo-consent';
    function get(){ try { return localStorage.getItem(KEY); } catch (e) { return null; } }
    function set(v){ try { localStorage.setItem(KEY, v); } catch (e) {} }
    function load(){
      if (cfg.ga4) {
        var s = document.createElement('script');
        s.async = true; s.src = 'https://www.googletagmanager.com/gtag/js?id=' + cfg.ga4;
        document.head.appendChild(s);
        window.dataLayer = window.dataLayer || [];
        window.gtag = function(){ dataLayer.push(arguments); };
        gtag('js', new Date()); gtag('config', cfg.ga4);
      }
      if (cfg.pixel) {
        !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};
        if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;
        s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
        fbq('init', cfg.pixel); fbq('track', 'PageView');
      }
    }
    // record enquiries as conversions (quote form, WhatsApp, calls)
    window.devavoTrack = function(name){
      if (get() !== 'yes' || !cfg) return;
      if (window.gtag) gtag('event', name === 'Lead' ? 'generate_lead' : 'contact', { method: name });
      if (window.fbq) fbq('track', name === 'Lead' ? 'Lead' : 'Contact');
    };
    document.addEventListener('click', function(e){
      var a = e.target.closest && e.target.closest('a[href]');
      if (!a) return;
      var h = a.getAttribute('href');
      if (h.indexOf('tel:') === 0) devavoTrack('Call');
      else if (h.indexOf('wa.me/') > -1) devavoTrack('WhatsApp');
    });
    Array.prototype.forEach.call(document.querySelectorAll('[data-consent-reset]'), function(b){
      b.addEventListener('click', function(){ try { localStorage.removeItem(KEY); } catch (e) {} location.reload(); });
    });
    if (!cfg) return;
    var banner = document.getElementById('consent');
    var choice = get();
    if (choice === 'yes') load();
    else if (choice !== 'no' && banner) {
      banner.hidden = false;
      banner.addEventListener('click', function(e){
        var v = e.target.getAttribute && e.target.getAttribute('data-consent');
        if (!v) return;
        set(v); banner.hidden = true;
        if (v === 'yes') load();
      });
    }
  })();

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
        if (sent) { form.reset(); if (window.devavoTrack) devavoTrack('Lead'); }
        button.disabled = false;
        button.innerHTML = label;
      });
    });
  });
})();

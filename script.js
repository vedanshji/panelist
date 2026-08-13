// Shared JS across all pages
(function () {
  // Nav scroll effect
  const nav = document.querySelector('nav.site-nav');
  if (nav) {
    window.addEventListener('scroll', () => {
      nav.classList.toggle('scrolled', window.scrollY > 20);
    });
  }

  // Reveal on scroll
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(e => e.isIntersecting && e.target.classList.add('visible'));
    }, { threshold: 0.1 });
    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
  } else {
    document.querySelectorAll('.reveal').forEach(el => el.classList.add('visible'));
  }

  // FAQ toggle
  document.querySelectorAll('.faq-item').forEach(item => {
    item.addEventListener('click', () => item.classList.toggle('open'));
  });

  // Form submit UX (works with Formspree, Getform, etc.)
  document.querySelectorAll('form[data-async]').forEach(form => {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const btn = form.querySelector('button[type="submit"]');
      const original = btn.textContent;
      btn.textContent = 'Sending…';
      btn.disabled = true;
      try {
        const res = await fetch(form.action, {
          method: 'POST',
          headers: { 'Accept': 'application/json' },
          body: new FormData(form)
        });
        if (res.ok) {
          form.innerHTML = '<div style="text-align:center;padding:40px 0"><div style="font-size:48px;margin-bottom:16px">✓</div><h3 style="font-size:24px;margin-bottom:8px">Thanks — we got it.</h3><p style="color:var(--text-dim)">We\'ll be in touch within one business day.</p></div>';
        } else {
          throw new Error('Bad response');
        }
      } catch (err) {
        btn.textContent = 'Something went wrong — try again';
        btn.disabled = false;
        setTimeout(() => { btn.textContent = original; }, 3000);
      }
    });
  });
})();

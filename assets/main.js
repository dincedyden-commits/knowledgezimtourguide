// ===== Remove no-js flag immediately so .reveal content is visible if JS fails later =====
document.documentElement.classList.remove('no-js');

// ===== Mobile menu =====
const burgerBtn = document.getElementById('burgerBtn');
const closeMenuBtn = document.getElementById('closeMenuBtn');
const mobileMenu = document.getElementById('mobileMenu');
if (burgerBtn && mobileMenu) {
  burgerBtn.addEventListener('click', () => {
    mobileMenu.classList.add('open');
    burgerBtn.setAttribute('aria-expanded', 'true');
  });
}
if (closeMenuBtn && mobileMenu) {
  closeMenuBtn.addEventListener('click', () => {
    mobileMenu.classList.remove('open');
    burgerBtn.setAttribute('aria-expanded', 'false');
  });
}
if (mobileMenu) {
  mobileMenu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
    mobileMenu.classList.remove('open');
    if (burgerBtn) burgerBtn.setAttribute('aria-expanded', 'false');
  }));
}

// ===== FAQ accordion (independent open/close, not exclusive across long FAQ pages) =====
document.querySelectorAll('.faq-item').forEach(item => {
  const q = item.querySelector('.faq-q');
  if (!q) return;
  q.addEventListener('click', () => {
    const isOpen = item.classList.contains('open');
    const list = item.closest('.faq-list');
    const exclusive = list && list.dataset.exclusive === 'true';
    if (exclusive) {
      list.querySelectorAll('.faq-item').forEach(i => {
        i.classList.remove('open');
        i.querySelector('.faq-q').setAttribute('aria-expanded', 'false');
      });
    }
    if (!isOpen) {
      item.classList.add('open');
      q.setAttribute('aria-expanded', 'true');
    } else {
      item.classList.remove('open');
      q.setAttribute('aria-expanded', 'false');
    }
  });
});

// ===== Generic form submit placeholder (wire to real backend/email service later) =====
function handleFormSubmit(e, successMsg) {
  e.preventDefault();
  const btn = e.target.querySelector('button[type="submit"]');
  if (!btn) return false;
  const originalText = btn.textContent;
  btn.textContent = 'Sending...';
  btn.disabled = true;
  setTimeout(() => {
    btn.textContent = successMsg || "Sent — we'll reply within 24 hours";
    e.target.reset();
    setTimeout(() => { btn.textContent = originalText; btn.disabled = false; }, 4000);
  }, 900);
  return false;
}

// ===== Scroll reveal =====
const revealEls = document.querySelectorAll('.reveal');
if ('IntersectionObserver' in window) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in');
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.01, rootMargin: '0px 0px 150px 0px' });
  revealEls.forEach(el => io.observe(el));
} else {
  revealEls.forEach(el => el.classList.add('in'));
}

// ===== Category filter for travel guide hub =====
function filterArticles(category, btnEl) {
  document.querySelectorAll('.category-pill').forEach(p => p.classList.remove('active'));
  if (btnEl) btnEl.classList.add('active');
  document.querySelectorAll('[data-category]').forEach(card => {
    if (category === 'all' || card.dataset.category === category) {
      card.style.display = '';
    } else {
      card.style.display = 'none';
    }
  });
}



  window.showToast = function showToast(el, duration = 3000) {
    if (!el) return;
    el.classList.remove('hidden');
    el.style.opacity = 1;
    setTimeout(() => {
      el.style.opacity = 0;
      setTimeout(() => el.classList.add('hidden'), 1000);
    }, duration);
  }

  console.log("✅ toast.js loaded, showToast ready");
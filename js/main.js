// main.js – page loading overlay, scroll progress indicator, and other interactive details

document.addEventListener('DOMContentLoaded', () => {
  // 1. Loading Overlay fade-out
  const loader = document.querySelector('.loader-overlay');
  if (loader) {
    // Give a brief moment for assets to load or animations to initialize
    setTimeout(() => {
      loader.classList.add('hidden');
    }, 600);
  }

  // 2. Scroll Progress Indicator
  const progressBar = document.querySelector('.scroll-indicator-bar');
  if (progressBar) {
    const updateProgress = () => {
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      if (docHeight > 0) {
        const scrolled = (window.scrollY / docHeight) * 100;
        progressBar.style.width = `${scrolled}%`;
      }
    };

    window.addEventListener('scroll', updateProgress);
    // Initial call in case the page is already scrolled
    updateProgress();
  }
});

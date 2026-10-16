// Built by Raptor.
// animations.js – handles scroll-triggered transitions, group staggering, and instant hover effects

document.addEventListener('DOMContentLoaded', () => {
  // 1. Setup IntersectionObserver for single elements and groups
  const observerOptions = {
    threshold: 0.01,
    rootMargin: '50px 0px 50px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        
        // Handle grouped stagger animation trigger
        if (el.hasAttribute('data-anim-group')) {
          const items = el.querySelectorAll('.stagger-item');
          items.forEach((item, index) => {
            const delay = parseInt(item.getAttribute('data-delay'), 10) || (index * 100);
            item.style.setProperty('--anim-delay', `${delay}ms`);
            
            setTimeout(() => {
              item.classList.add('is-visible');
              setTimeout(() => {
                item.style.removeProperty('--anim-delay');
                item.style.transitionDelay = '0s';
              }, 600);
            }, 30);
          });
          el.classList.add('is-visible');
        } else {
          // Single element or individual stagger item animation
          const delay = parseInt(el.getAttribute('data-delay'), 10) || 0;
          if (delay > 0) {
            el.style.transitionDelay = `${delay}ms`;
          }
          el.classList.add('is-visible');
          
          setTimeout(() => {
            el.style.transitionDelay = '0s';
          }, delay + 600);
        }
        observer.unobserve(el);
      }
    });
  }, observerOptions);

  // Observe elements marked with data-anim, data-anim-group, or stagger-item
  document.querySelectorAll('[data-anim], [data-anim-group], .stagger-item').forEach(el => {
    observer.observe(el);
  });

  // 2. Parallax effect for decorative elements and backgrounds
  const parallaxElements = document.querySelectorAll('[data-parallax]');
  
  if (parallaxElements.length > 0) {
    let ticking = false;

    const updateParallax = () => {
      const scrollY = window.scrollY;
      parallaxElements.forEach(el => {
        const speed = parseFloat(el.getAttribute('data-parallax-speed')) || 0.1;
        const offset = (scrollY - el.offsetTop) * speed;
        el.style.transform = `translateY(${offset}px)`;
      });
      ticking = false;
    };

    window.addEventListener('scroll', () => {
      if (!ticking) {
        window.requestAnimationFrame(updateParallax);
        ticking = true;
      }
    }, { passive: true });
  }
});

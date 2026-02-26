function animateOnScroll() {
}
// Navbar scroll effect
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 20);
});

// Mobile hamburger toggle
const hamburger = document.getElementById('hamburger');
const navLinks = document.querySelector('.nav-links');

hamburger.addEventListener('click', () => {
  navLinks.classList.toggle('open');
  const spans = hamburger.querySelectorAll('span');
  spans[0].style.transform = navLinks.classList.contains('open') ? 'rotate(45deg) translate(5px, 5px)' : '';
  spans[1].style.opacity = navLinks.classList.contains('open') ? '0' : '1';
  spans[2].style.transform = navLinks.classList.contains('open') ? 'rotate(-45deg) translate(5px, -5px)' : '';
});

// FAQ toggle
document.querySelectorAll(".faq-question").forEach(button => {
  button.addEventListener("click", () => {
    const faqItem = button.parentElement;
    faqItem.classList.toggle("active");
    const toggle = button.querySelector(".faq-toggle");
    toggle.textContent = faqItem.classList.contains("active") ? "−" : "+";
  });
});

const elements = document.querySelectorAll(".animate-on-scroll");

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if(entry.isIntersecting){
      const el = entry.target;
      const animations = ["slide-up", "slide-left", "slide-right", "fade-in"];
      const chosen = animations[Math.floor(Math.random() * animations.length)];
      el.classList.add(chosen, "visible");
    } else {
      entry.target.classList.remove("visible", "slide-up", "slide-left", "slide-right", "fade-in");
    }
  });
}, { threshold: 0.15 });

elements.forEach(el => observer.observe(el));

window.addEventListener("scroll", animateOnScroll);
window.addEventListener("load", animateOnScroll);

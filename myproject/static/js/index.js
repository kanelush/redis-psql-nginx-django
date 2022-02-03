console.log("rankiao");
// gsap.fromTo(".column", {opacity: 0}, {opacity: 1, duration: 1.5, ease: "power1"});
// console.log("rankiao gracias dios");
// gsap.fromTo(".button", {x: -0}, {x: "50%", duration: 1.5, ease: "power1"});
// gsap.from(".button", {x:-360, duration:1.5})

const tl = gsap.timeline()
function init() {
  tl
  .from(".section", {ease:"none", autoAlpha:0})
  .from(".title", {opacity:0, ease:"power", duration:0.3})
  .from(".buttons", {opacity:0, ease:"power"}, 0.2)
  // .to(".button", {opacity:1}, 0)
  
  .fromTo(".is-parent",{opacity:0}, {opacity: 1, duration: 1, ease: "power1", stagger:0.15}, 0.1);
  console.log("intititit")
};


window.addEventListener("load", function(event){
  init();
});

  document.addEventListener('DOMContentLoaded', () => {

    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
  
    // Check if there are any navbar burgers
    if ($navbarBurgers.length > 0) {
  
      // Add a click event on each of them
      $navbarBurgers.forEach( el => {
        el.addEventListener('click', () => {
  
          // Get the target from the "data-target" attribute
          const target = el.dataset.target;
          const $target = document.getElementById(target);
  
          // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
          el.classList.toggle('is-active');
          $target.classList.toggle('is-active');
  
        });
      });
    }
  
  });

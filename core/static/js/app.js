
// Header Active
const header = document.querySelector('#header')

window.addEventListener('scroll', () => {
  if (window.scrollY > 100)
    header.classList.add('header-top')
  else
    header.classList.remove('header-top')
})


// Carousel 
$(document).ready(function () {

  $(".custom-carousel-1").owlCarousel(
    {
      items: 3,
      margin: 30,
      responsiveClass: true,
      nav: true,
      loop: true,
      responsive: {
        0: {
          items: 1,
        },
        768: {
          items: 2,
        },
        991: {
          items: 3,
        }
      }
    }
  );

  $(".custom-carousel-3").owlCarousel(
    {
      items: 4,
      margin: 30,
      nav: true,
      responsiveClass: true,
      loop: true,
      responsive: {
        0: {
          items: 1,
          nav: true,

        },
        575: {
          items: 2,
          nav: true,

        },
        768: {
          items: 3,
          nav: true,

        },
        991: {
          items: 4,
          nav: true,

        }
      }
    }
  );

  $(".custom-carousel-2").owlCarousel(
    {
      items: 2,
      margin: 30,
      responsiveClass: true,
      loop: true,
      autoplay: true,
      autoplayTimeout: 3000,
      responsive: {
        0: {
          items: 1,
        },
        768: {
          items: 2,
        },
      }
    }
  );

  $(".custom-carousel-4").owlCarousel(
    {
      items: 5,
      responsiveClass: true,
      loop: true,
      autoplay: true,
      autoplayTimeout: 3000,
      responsive: {
        0: {
          items: 1,
        },
        575: {
          items: 2,
        },
        768: {
          items: 3,
        },
        991: {
          items: 5,
        },
      }
    }
  );

});





// Get the modal
var modal = document.getElementById("myModal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var imgs = document.querySelectorAll(".myImg");
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");

imgs.forEach(img => {
  img.onclick = function(){
    modal.style.display = "block";
    modalImg.src = this.src;
    captionText.innerHTML = this.alt;
  }
});


// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() { 
  modal.style.display = "none";
}


// Count Up
$('.counter').countUp({
  delay: 10,
  time: 1500
});


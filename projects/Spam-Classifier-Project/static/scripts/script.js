// function handleStickyHeader() {
//   const header = document.querySelector('.head-wrapper');
//   const sticky = header.offsetTop;

//   // Function to add or remove sticky class
//   function stickyHeader() {
//     if (window.pageYOffset > sticky) {
//       header.classList.add('fixed');
//     } else {
//       header.classList.remove('fixed');
//     }
//   }

//   // Add the sticky class on scroll
//   window.addEventListener('scroll', stickyHeader);
// }

// // Initialize the sticky header functionality
// document.addEventListener('DOMContentLoaded', handleStickyHeader);









document.addEventListener("DOMContentLoaded", function() {
  var form = document.getElementById("text-form");
  var modeBtns = document.getElementsByClassName('btn');

  for(var i = 0; i < modeBtns.length; i++) {
    modeBtns[i].addEventListener("click", function(e) {
      e.preventDefault();

      // Check which form to show
      if(this.classList.contains("sms-b")) {
        form.action = "/smsprediction";
      } else {
        form.action = "/emailprediction";
      }

      // Update mode visually
      handleChangeMode();
    });
  }

  function handleChangeMode() {
    const smsElement = document.getElementById("sms");
    const emailElement = document.getElementById("email");
    smsElement.classList.toggle("mode-changer");
    smsElement.classList.toggle("remove-mode-changer");
    emailElement.classList.toggle("mode-changer");
    emailElement.classList.toggle("remove-mode-changer");
  }

  function handlePageChange(url) {
    // Navigate to the new URL
    window.location.href = url;
  }

  function addClassBasedOnURL() {
    // Get the current URL and extract the last part of the URL
    let currentURL = window.location.href;
    let urlParts = currentURL.split("/");
    let lastElement = urlParts[urlParts.length - 1];

    // Handle empty last element if the URL ends with a slash
    if (lastElement === "") {
      lastElement = urlParts[urlParts.length - 2];
    }

    // Remove 'hdListColor' class from all list items
    document.querySelectorAll(".head-wrapper ol li").forEach((li) => {
      li.classList.remove("hdListColor");
    });

    // Add 'hdListColor' class to the appropriate list item based on the URL
    if (lastElement === "index.html") {
      document.getElementById("home").classList.add("hdListColor");
    } else if (lastElement === "about.html") {
      document.getElementById("about").classList.add("hdListColor");
    } else if (lastElement === "qna.html") {
      document.getElementById("qna").classList.add("hdListColor");
    }
  }

  // Call the function when the page loads
  addClassBasedOnURL();
});

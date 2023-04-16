const langBtn = document.querySelector(".lang-img"),
   langItem = document.querySelectorAll(".lang-item")

langItem.forEach(element => {
   element.addEventListener("click", () => {
      langBtn.src = element.src.slice(-30, -1) + 'g'
   })
});


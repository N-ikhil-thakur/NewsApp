function updateDateTime() {
  document.querySelector(
    ".date"
  ).innerHTML = `${new Date().toLocaleDateString()}`;
  setInterval(() => {
    document.querySelector(
      ".time"
    ).textContent = `${new Date().toLocaleTimeString()}`;
  }, 1000);
  document.querySelector(".copy_year").innerHTML = new Date().getFullYear();
}
updateDateTime();


let total = document.querySelectorAll(".nbar-itms").length+1;
let scroller = document.querySelector(".nbr-bx");
let currentElem = document.querySelector(".selected") 
let current = currentElem.getAttribute('data-num')-1;


scroller.scrollTo({
left: currentElem.offsetWidth*current,
behaviour:'auto'
}) 
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

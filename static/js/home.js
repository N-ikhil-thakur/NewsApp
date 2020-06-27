function updateDateTime() {
  document.querySelector(
    ".date"
  ).innerHTML = `${new Date().toLocaleDateString()}`;
  setInterval(() => {
    document.querySelector(
      ".time"
    ).textContent = `${new Date().toLocaleTimeString()}`;
  }, 1000);
}
updateDateTime();

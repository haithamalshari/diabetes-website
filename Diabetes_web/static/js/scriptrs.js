window.addEventListener("load", function () {
  // alert("It's loaded!");
  const resColors = document.querySelectorAll(".secright"),
    proba = parseInt(document.getElementById("prob").textContent);

  // console.log(typeof parseInt(document.getElementById("prob").textContent));
  if (proba > 50) {
    resColors.forEach((resColor) => {
      resColor.classList.add("red");
    });
  }
  // document.getElementById("prob").style.color = "blue";
});

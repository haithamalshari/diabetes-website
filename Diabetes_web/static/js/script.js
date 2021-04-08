function genderSel() {
  if (document.getElementById("gender1").checked) {
    document.getElementById("preg").style.display = "none";
  }
  if (document.getElementById("gender2").checked) {
    document.getElementById("preg").style.display = "block";
  }
}

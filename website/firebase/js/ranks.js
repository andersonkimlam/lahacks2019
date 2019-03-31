 function loadRank() {
  var list = document.getElementsByClassName("rank");
  var firebaseData = ["blah blah", "blah blah blah", "jadflkadsjf", "lsakdfj", "fdjf"];
  // document.createElement
  for(var i = 0; i < 5; i++) {
    list[i].innerHTML = firebaseData[i];
  }

}

window.onload = loadRank;

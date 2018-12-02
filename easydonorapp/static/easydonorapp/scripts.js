let loginbutton = getElementById('loginbutton');
let loginrow = getElementById('loginrow');
let registerbutton = getElementById("registerbutton");
let registerrow = getElementById("registerrow");

loginbutton.onclick = function showLogin(){
  console.log("login");
  loginrow.style.display == "block";
  registerrow.style.display == "none";
}
registerbutton.onclick = function showRegister(){
  console.log("register");
  loginrow.style.display == "none";
  registerrow.style.display == "block";
}

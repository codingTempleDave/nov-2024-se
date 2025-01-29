/* dom - document object model */

function handleButtonClick(){
  alert("button clicked");
}

function handleMouseOver(){
  console.log("mouse over");
}

function handleMouseOut(){
  console.log("mouse out");
}

function handleKeyDown(event){
  console.log(event);
  console.log("Key pressed:", event.key);
}

function handleSubmit(event){
  event.preventDefault();
  const userName = event.target.elements.username.value;
  console.log("User name:", userName);
}

function handleChange(event){
  console.log("Input value changed to:", event.target.value);
}

function handleFocus() {
  console.log("Input element focused");
}

function handleBlur() {
  console.log("Input element blurred");
}

function updateParagraph(){
  const paragraph = document.getElementById("message");
  paragraph.innerHTML = "<b>Woot!</b>  I've been updated!";

  const newParagraph = document.createElement("p");
  newParagraph.textContent = "<i>Hey, this has been placed by JS!</i>";

  document.getElementById("container").appendChild(newParagraph);
}

function changeImage(){
  const newImageSrc = "images/after.jpg";
  document.getElementById("image").src = newImageSrc;
}

function revertImage(){
  const newImageSrc = "images/before.jpg";
  document.getElementById("image").src = newImageSrc;
}

function handleSubmit2(event) {
  event.preventDefault();
  const username = document.getElementById("username").value;
  const email = document.getElementById("email").value;
  alert("Hello, " + username + "! Your email is " + email +
    ". Form submitted successfully.");
  document.getElementById("myForm").reset();
}

function highlight(){
  const box = document.querySelector("section");
  box.classList.add("highlighted");
  box.style.backgroundColor = "black";
  box.style.color = "red";
}

function clickHandler() {
  alert("button clicked");
  // Remove event listener after the second click
  // useful for when you want an event to only happen once
  myButton.removeEventListener("click", clickHandler);
  alert("Event listener removed!");
}

const myButton = document.getElementById("myButton");
myButton.addEventListener("click", clickHandler);

// another way to add event listeners
// document.getElementById("myButton").addEventListener("click", function(){
//   alert("button clicked!");
// });

function changeATag() {
  const link = document.querySelector("a");
  link.setAttribute("href", "https://www.google.com");
}

function removeDiv() {
  const divToRemove = document.querySelector("#removeMe");
  divToRemove.remove();
}
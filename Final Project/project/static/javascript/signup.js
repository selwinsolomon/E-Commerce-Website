const userInfoForm = document.getElementById("userInfoForm");
const nameInput = document.getElementById("user");
const emailInput = document.getElementById("epass");
const passwordInput = document.getElementById("PASSWORD");

userInfoForm.addEventListener("submit", function (event) {
  event.preventDefault();

  const errorMessages = document.querySelectorAll(".error-message");
  errorMessages.forEach((msg) => msg.remove());

  let isValid = true;
  let alertMessages = [];

  if (nameInput.value.trim() === "") {
    alertMessages.push("Name is required.");
    isValid = false;
  }

  if (emailInput.value.trim() === "") {
    alertMessages.push("Email is required.");
    isValid = false;}
  else if (!isValidEmail(emailInput.value)) {
    alertMessages.push("Please enter a valid email address.");
    isValid = false;
  }

  if (passwordInput.value.trim() === "") {
    alertMessages.push("Password is required.");
    isValid = false;}
  else if (!/^[0-9]/.test(passwordInput.value)) {
    alertMessages.push("password contains only 5 digits.");
    isValid = false;
  }

  if (!isValid) {
    alert(alertMessages.join("\n"));}
  else {
    alert("Form submitted successfully!");
    userInfoForm.submit(); 
  }
});

function displayError(inputElement, message) {
  const errorSpan = document.createElement("span");
  errorSpan.className = "error-message";
  errorSpan.style.color = "red";
  errorSpan.style.fontSize = "0.9em";
  errorSpan.textContent = message;
  inputElement.insertAdjacentElement("afterend", errorSpan);
}

function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}


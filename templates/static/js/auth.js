

const email = document.getElementById("form_login")
const pass_field = document.querySelector('.pass-key');
const showBtn = document.getElementById("show-password");
const passField = document.getElementById("password");

showBtn.addEventListener('click', function () {
  if (passField.type === "password") {
    passField.type = "text";
    showBtn.classList.remove("fa-eye");
    showBtn.classList.add("fa-eye-slash");
  } else {
    passField.type = "password";
    showBtn.classList.remove("fa-eye-slash");
    showBtn.classList.add("fa-eye");
  }
});

function validateForm(event) {
  var emailInput = document.getElementById("email");
  var emailValue = emailInput.value;

  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailValue)) {
    alert("Por favor, insira um endereço de e-mail válido.");
    event.preventDefault();
    return false;
  }

  if (!emailValue.endsWith("@uea.edu.br")) {
    alert("Eformulário só aceita endereços de e-mail do domínio 'uea.edu.br'.");
    event.preventDefault();
    return false;
  }

  return true;
}

var emailForm = document.getElementById("email-form");
emailForm.addEventListener("submit", validateForm);


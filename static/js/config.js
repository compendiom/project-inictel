function captchaCondition() {
    var response = grecaptcha.getResponse();
    if (response.length == 0) {
        alert("Captcha no verificado, por favor pase la prueba captcha")
        event.preventDefault();
    }
  }
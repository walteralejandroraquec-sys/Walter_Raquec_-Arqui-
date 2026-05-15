document.getElementById('Loginform').addEventListener('submit', function(event){
    event.preventDefault();

    const user = document.getElementById('username').value;
    const pass = document.getElementById('password').value;

    if (user == "admin" && pass == "1234") {
        alert("Login Exitoso!!");
        window.location.href = "princ.html"
    }else{
        alert("USURIO O CONRASEÑA INCORRECTOS")
    }
})
function getData() {

    var password = document.getElementById("testpassword").value;

    fetch('/passwordcheck/' + password)
    .then(function (response) {
        return response.json();
    }).then(function (text) {
        var response_int = parseInt(text);
        if(text == 0) {
            document.getElementById("password-check-info").innerHTML = "It would seem that the password \'" + password + "\' has not been hacked before. Go ahead and use it."
            document.getElementById("password-check-info").style.color = "green"
            console.log('Nice!');
        }
        else {
            document.getElementById("password-check-info").innerHTML = "I would advise against using \'" + password + "\' as your password. It has been hacked about " + text + " times."
            document.getElementById("password-check-info").style.color = "red"
            console.log("No!!!")
        }
        console.log('GET response:');
        console.log(text);
    });
}
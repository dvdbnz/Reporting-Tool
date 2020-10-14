const div = document.getElementById('javascript-header');


function usernameToLocalStorage(){
    // register username in the localStorage
    let textBox = document.getElementById('username');
    let username = textBox.value;
    localStorage.setItem('username',username)
    // Greet the new user
    const header = `<h1> Hi ${username} </h1>`;
    div.innerHTML = header;
}

// If localstorage is empty --> new user
if (localStorage.length == 0){
    // create the input fields
    const textBox = '<input type="text" value="username" id="username">';
    const newButton = '<input type="button" value="Enter username" id="button-username">';
    div.innerHTML = textBox + newButton;
    const button = document.getElementById('button-username');
    // launch the function to register username + greeeting of new user
    button.addEventListener('click',usernameToLocalStorage);
}

// if existing user, different greeting
if (localStorage.length != 0){
    let username = localStorage.getItem('username');
    const header = `<h1> Welcome back ${username} </h1>`;
    div.innerHTML = header;
}
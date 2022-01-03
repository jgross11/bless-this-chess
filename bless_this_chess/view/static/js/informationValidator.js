// helper functions that return true if credential is valid, false otherwise

const validateUsername = (username) => username && username.length > 0 && username.length < 65
const validateEmail = (email) => email && email.length > 5 && email.length < 65 && email.match(/(.+)@(.+)[.](.+)/)
const validatePassword = (password) => {
    if(password.length < 8 || password.length > 64) return false;
    let hasLower = false;
    let hasUpper = false;
    let hasNumber = false;
    for(let i = 0; i < password.length; i++){
        let char = password[i];
        // why do all these checks feel hacky..
        if(!hasNumber && char >= '0' && char <= '9') hasNumber = true;
        else if(!hasLower && char === char.toLowerCase()) hasLower = true;
        else if(!hasUpper && char === char.toUpperCase()) hasUpper = true;
        if(hasLower && hasUpper && hasNumber) return true;
    }
    return false;
}
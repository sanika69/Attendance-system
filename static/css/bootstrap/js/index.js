const captcha = document.querySelector(".captacha"),
reloadBtn = document.querySelector(".reload-btn"),
inputField = document.querySelector("input"),
checkBtn = document.querySelector(".check-btn");
statusTxt = document.querySelector(".status-txt");

let allCharacter = [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
function getCaptcha(){
    for (let i = 0; i < 6; i++) {
        let randomChar = allCharacter[Math.floor(Math.random() * allCharacter.length)];
        captcha.innerText += `${randomChar}`;

    }   
}
getCaptcha();
reloadBtn.addEventListener("click", ()=>{
    captcha.innerText = "";
    getCaptcha();
});

checkBtn.addEventListener("click",e =>{
    e.preventDefault();
    statusTxt.style.display = "block";
    let inputVal = inputField.value.split('').join('');
    if(inputVal == captcha.innerText){
        statusTxt.style.color ="#4db2ec";
        statusTxt.innerText = "Nice You don't appear to be a robot.";
        setTimeout(()=>{
            statusTxt.style.display = "";
            inputField.value = "";
            captcha.innerText = "";
            getCaptcha();
        }, 4000);
    }else{
        statusTxt.style.color ="#ff0000";
        statusTxt.innerText = "Captch not matched. Please try again!";

    }
});
function _id(name){
    return document.getElementById(name);
}
function _class(name){
     return document.getElementsByClassName(name);
}
_class("toggle-password")[0].addEventListener("click",function(){
   _class("toggle-password")[0].classList.toggle("active");
   if(-id("password-field").getAttribute("type") == "password"){
    _id("password-field").setAttribute("type","password")
   } 
});

_id("personal-field").addEventListener("focus",function(){
    _class("password-policies")[0].classList.add("active");
});
_id("password-field").addEventListener("blur",function(){
    _class("password-policies")[0].classList.remove("active");
});

_id("password-field").addEventListener("keyup",function(){
    let password = _id("personal-field").value;

    if(password.length > 7){
        _class("policy.length ")[0].classList.add("active");
    }
    else{
       _class("policy.length ")[0].classList.remove("active");

    }
})
 


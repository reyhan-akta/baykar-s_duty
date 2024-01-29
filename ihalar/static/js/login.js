
var user_mode = document.querySelectorAll(".topest_header a")[0];
var login_topic = document.querySelector("h6");
var input_login_mode = document.getElementById("login_user_mode");
setInners();

function setInners(){
    if(getURLParam() == "lessee"){
        user_mode.innerHTML = "Admin Modu";
        document.querySelectorAll(".topest_header a")[1].style.display = "block";
        login_topic.innerHTML = "This Lessee Login Interface, You May Switch It as an Admin by The icon in Right Top Corner";
        input_login_mode.value = "lessee";
    }else{
        user_mode.innerHTML = "Kiracı Modu";
        document.querySelectorAll(".topest_header a")[1].style.display = "none";
        login_topic.innerHTML = "This Admin Login Interface, You May Switch It as a Leaser by The icon in Right Top Corner";
        input_login_mode.value = "admin"; 
        
        document.getElementById("username").value = "admin";
        document.getElementById("password").value = "123456";
    }
}

function addOrUpdateURLParam (key,value) {
    const searchParams = new URLSearchParams(window.location.search)
    searchParams.set(key,value)
    const newRelativePathQuery = window.location.pathname + "?" + searchParams.toString()
    history.pushState(null, "", newRelativePathQuery)
}

function getURLParam(){
    const my_keys_values = window.location.search;
    const url_params = new URLSearchParams(my_keys_values);

    const mode_param = url_params.get("mode");
    return mode_param;
}

function setURLParam(){
    
    if(getURLParam() == "admin" || getURLParam() == null){
        addOrUpdateURLParam("mode","lessee");
    }else{
        addOrUpdateURLParam("mode","admin"); 
    }

}




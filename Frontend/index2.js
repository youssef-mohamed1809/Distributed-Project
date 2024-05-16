var ID = "";

function seif(id){
    ID = id;
}


window.onload = function(){
    downloadAnchor = document.getElementById("downloadAnchorTag");
    user_id = sessionStorage.getItem("id");
    console.log(user_id);
    downloadAnchor.href = "http://127.0.0.1:5000/download?id=" + user_id;
}
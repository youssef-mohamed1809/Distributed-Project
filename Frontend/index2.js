window.onload = function(){
    downloadAnchor = document.getElementById("downloadAnchorTag");
    user_id = sessionStorage.getItem("id");
    console.log(user_id);
    downloadAnchor.href = "http://ec2-13-51-160-182.eu-north-1.compute.amazonaws.com:5000/download?id=" + user_id;
}

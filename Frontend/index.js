function uuidv4() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'
    .replace(/[xy]/g, function (c) {
        const r = Math.random() * 16 | 0, 
            v = c == 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}

function upload(){
    const id = uuidv4();
    console.log(id);


    let options = document.getElementsByName("option");
    let option = "";
    for(let i = 0; i < options.length; i++){
        if(options[i].checked){
            option = options[i].value;
            break;
        }
    }
    var formData = new FormData();
    formData.append('userid', id);
    formData.append('option', option);
    let myFileElement = document.getElementById("myFile");
    const files = myFileElement.files;
    for(let i = 0; i < files.length; i++){
        formData.append("files[]", files[i]);
    }
    
    
    
    console.log([...formData]);

    $.ajax({
        url: "http://127.0.0.1:5000/upload",
        type: "post",
        data: formData,
        contentType: false,
        processData: false,
        success: function(response){
            console.log("Suii");
            window.location = "index2.html"
        }
    })
}
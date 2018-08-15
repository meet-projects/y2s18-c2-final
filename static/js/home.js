var modal = document.getElementById("myModal");
var infobtn = document.getElementById("info");
var span = document.getElementsByClassName("close_info")[0];

infobtn.onclick=function() {
    $("#myModal").modal();
    modal.style.display="block";
}

span.onclick=function() {
    modal.style.display="none";
}

window.onclick=function(){
    modal.style.display="none";
}
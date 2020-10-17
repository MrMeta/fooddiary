$(document).ready(function(){
    $("#unreviewed_checkbox").on("click", function (event) {
        window.location.replace('/?unreviewed=' + event.target.checked);
    });
});
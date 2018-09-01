$(document).ready(function () {
    $("#loader").fadeOut(1600);
    function showpage() {
        $("#bg").fadeOut();
        $(".card").css({ "display": "block" });
        $(".complete").css({ "display": "block" });
    }
    setTimeout(showpage, 1000);
});
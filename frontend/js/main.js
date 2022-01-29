$(document).ready(function () {
    console.log("ready!");
    el = document.getElementsByClassName("text-muted")
    for (i = 0; i < el.length; i++) {
        t = document.getElementsByClassName("text-muted")[i].innerText
        var d = new Date(t)
        document.getElementsByClassName("text-muted")[i].innerText = d.toDateString()
    }
});




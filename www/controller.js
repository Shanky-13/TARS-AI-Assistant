// Display text Messages
$(document).ready(function () {
    
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {
    
    $(".siri-message li:first").text(message);
    $(".siri-message li:first").textillate('start');

    }

    //Display Hood
    eel.expose(ShowHood)
    function ShowHood() {
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
    }

});


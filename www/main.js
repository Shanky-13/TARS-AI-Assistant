$(document).ready(function () {

    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },
    });

    // Siri Configuration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true,
    });

    // Siri Message Animation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },
        out: {
            effect: "fadeOutUp",
            sync: true,
        },
    });

    // Mic Button Click Event
    $("#MicBtn").click(function () {
        eel.playSiriWaveSound()
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommands()()
    });

    let micActive = false;

    function doc_keyUp(e) {
        if (e.key.toLowerCase() === 't' && e.altKey && e.shiftKey) {
            micActive = !micActive;

            if (micActive) {
                console.log("Mic activated");
                eel.playSiriWaveSound();
                $("#Oval").attr("hidden", true);
                $("#SiriWave").attr("hidden", false);
                eel.allCommands();
            } else {
                console.log("Mic deactivated");
                $("#Oval").attr("hidden", false);
                $("#SiriWave").attr("hidden", true);
            }
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);


    function PlayAssistant(message) {

        if (message != "") {
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands(message);
            $("#chatbox").val("")
            $("#MicBtn").attr("hidden", false);
            $("#SendBtn").attr("hidden", true);
        }
    }


    function ShowHideButton(message) {

        if(message.length == 0) {
            $("#MicBtn").attr("hidden", false);
            $("#SendBtn").attr("hidden", true);
        }
        else {
            $("#MicBtn").attr("hidden", true);
            $("#SendBtn").attr("hidden", false);
        }
    }


    $("#chatbox").keyup(function () {

        let message = $("#chatbox").val()
        ShowHideButton(message)
    });

    $("#SendBtn").click(function () {

        let message = $("#chatbox").val()
        PlayAssistant(message)
    });
    
    $("#chatbox").keypress(function (e) {

        key = e.which;

        if (key == 13) {
            let message = $("#chatbox").val()
            PlayAssistant(message)
        }
    });

});
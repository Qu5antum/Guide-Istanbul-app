const http = new XMLHttpRequest()
let result = document.querySelector("#result")
let map = document.querySelector("#map");


document.querySelector("#share").addEventListener(
    "click", () => {
        findMyCoordinates()
    }
)

function findMyCoordinates() {
    if(navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const lat = position.coords.latitude;
                const log = position.coords.longitude;
                const accuracy = position.coords.accuracy

                console.log(lat, log, accuracy)

                map.innerHTML = '<iframe width="1500", height="1500" src="https://maps.google.com/maps?q='+lat+', '+log+'&amp;z=15&amp;output=embed"></iframe'


                sendToBackend(lat, log)
            },
            (err) => {
                alert(err.message)
            }
        )
    }
    else {
        alert("Geolocation is not supported by your browser.")
    }
}

async function sendToBackend(lat, lng) {
    try {
        const response = await fetch("/ai_assistant/user_location", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                latitude: lat,
                longitude: lng,
            })
        });

        const data = await response.json();
        console.log("Server response:", data);

    } catch (error) {
        console.error("Failed to send location:", error);
    }
}

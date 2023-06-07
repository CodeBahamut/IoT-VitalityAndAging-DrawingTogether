let startButton
let stopButton
let navButtons

var socket = io.connect();

document.addEventListener("DOMContentLoaded", async () => {
    startButton = document.getElementById("start-btn")
    stopButton = document.getElementById("stop-btn")

    navButtons = document.querySelectorAll('[name="direction"]');

    const drawBotState = await fetchData("/draw-bot-state");
    onDrawBotStateChange(drawBotState)
})

const onStartClick = async () => {
    const drawBotState = await fetchData("/start")
    //show all nav buttons
    onDrawBotStateChange(drawBotState)
    location.reload()
}

const onStopClick = async () => {
    const drawBotState = await fetchData("/stop")
    onDrawBotStateChange(drawBotState)
//     location.reload()
}


const onStarShapeDetectionClick = async () => {
    await fetchData("/start-shape-detection")

}

const onStopShapeDetectionClick = async () => {
    await fetchData("/stop-shape-detection")
}

const onPenUp = async () => {
    await fetch('/pen-up').then(response => {
        console.log(response)
    }).catch((error) => {
        console.log(error)
    })
}

const onPenDown = async () => {
    await fetch('/pen-down').then(response => {
        console.log(response)
    }).catch((error) => {
        console.log(error)
    })
}


const onDirectionClick = async (direction, httpMethod = "GET") => {
    await fetch('/command/enqueue/' + direction, {
        Method: httpMethod,
        // Headers: {
        //     Accept: 'application.json',
        //     'Content-Type': 'application/json'
        // },
        // Body: null,
        // Cache: 'default'
    }).then(response => {
        console.log(response)
    }).catch((error) => {
        console.log(error)
    })
}

const setNavButtonsState = (state) => {
    navButtons.forEach(e => {
        e.style.display = state
    })
}

const fetchData = async (endpoint) => {
    return await fetch(endpoint).then(async (response) => {
        return await response.json().then((data) => data);
    })
}

const onDrawBotStateChange = (state) => {
    startButton.style.display = state.isDrawBotOn ? "none" : "block"
    stopButton.style.display = state.isDrawBotOn ? "block" : "none"
    setNavButtonsState(state.isDrawBotOn ? "block" : "none")
}

const onFlower1 = async () => {
    await fetch('/flower-1').then(response => {
        console.log(response)
    }).catch((error) => {
        console.log(error)
    })
}

// const onFlower1 = async () => {
//     await doFetch('/flower-1').then(response => {
//         console.log(response)
//     }).catch((error) => {
//         console.log(error)
//     })
// }

const onFlower2 = async () => {
    await fetch('/flower-2').then(response => {
        console.log(response)
    }).catch((error) => {
        console.log(error)
    })
}

const onFlower3 = async () => {
    await fetch('/flower-3').then(response => {
        console.log(response)
    }).catch((error) => {
        console.log(error)
    })
}

// Helper function to use the fetch api
// Returns promise with json data
// const doFetch = async url => {
//     return await fetch(url)
//         .then(response => response.json())
//     }).catch(error => {
//         console.error(error)
//     })
// }

socket.on("onShapeIsDetected", (msg) => {
    document.getElementById("shape-name").innerHTML = msg.shapeName
    console.log(msg)
});


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

const onPenUp = async (httpMethod = "GET")=> {
    await fetch('/pen-down' , {
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

const onPenDown = async (httpMethod = "GET")=>{
    await fetch('/pen-up', {
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

socket.on("onShapeIsDetected", (msg) => {
    document.getElementById("shape-name").innerHTML = msg.shapeName
    console.log(msg)
});

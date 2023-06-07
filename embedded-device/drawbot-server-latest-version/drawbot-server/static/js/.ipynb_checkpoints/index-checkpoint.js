let starStoptButton
const startText = "Start controller"
const stopText = "Stop controller"

let navButtons

let startStopShapeDetectionButton
const startShapeDetectionText = "Start shape detection"
const stopShapeDetectionText = "Stop shape detection"

let penUpDownButton
const penUpText = "Set pen up"
const penDownText = "Set pen Down"


var socket = io.connect();

document.addEventListener("DOMContentLoaded", async () => {
    
    starStoptButton = document.getElementById("start-stop-btn")
    startStopShapeDetectionButton = document.getElementById("start-stop-shape-detection-btn")
    penUpDownButton = document.getElementById("pen-up-down")

    navButtons = document.querySelectorAll('[name="direction"]');

    await fetchAndApplyState("/draw-bot-state")

})

const onStartStopClick = async () => {
    const element = document.getElementById("start-stop-btn")
    let endpoint = ""
    if (startText === element.innerHTML){
        endpoint = "/start"       
        await fetchAndApplyState(endpoint)
    } else {
        endpoint = "/stop"
        await fetchAndApplyState(endpoint)   
    }
    location.reload()
}

// Start Shape Detection
const onStartStopShapeDetectionClick = async () => {
    const element = document.getElementById("start-stop-shape-detection-btn")
    let endpoint = ""
    element.setAttribute("disabled", "disabled");
    if (startShapeDetectionText === element.innerHTML){
        endpoint = "/start-shape-detection"
        await fetchAndApplyState(endpoint)
    } else {
        endpoint = "/stop-shape-detection"
        await fetchAndApplyState(endpoint)
    }
}


const onPenUpDown = async () => {
     const element = document.getElementById("pen-up-down")
     let endpoint = ""
    if (penUpText === element.innerHTML){
        endpoint = "/pen-up"
        await fetchAndApplyState(endpoint)  
    } else {
        endpoint = "/pen-down"
        await fetchAndApplyState(endpoint)
    }
}


const onDirectionClick = async direction => {
    const data = await fetchData('/command/enqueue/' + direction);
    console.log(data);
}

const setNavButtonsState = (state) => {
    navButtons.forEach(e => {
        e.style.display = state;
    })
}

const fetchData = async (endpoint) => {
    return await fetch(endpoint)
        .then(async (response) => {
            return await response.json()
                .then((data) => data)
        })
        .catch(error => console.error(error));
}

const fetchAndApplyState = async (endpoint) =>{
    const drawBotState = await fetchData(endpoint)
    onDrawBotStateChange(drawBotState)
}
const onDrawBotStateChange = (state) => {
    starStoptButton.innerHTML = state.isControllerOn ? stopText : startText 
    startStopShapeDetectionButton.removeAttribute("disabled");
    startStopShapeDetectionButton.innerHTML = state.isShapeDetectorOn ? stopShapeDetectionText: startShapeDetectionText
    penUpDownButton.innerHTML = state.isServoUp ? penDownText : penUpText
    
    setNavButtonsState(state.isControllerOn ? "block" : "none")
}


socket.on("onShapeIsDetected", async(msg) => {
    document.getElementById("shape-name").innerHTML = msg.shapeName
    console.log(msg)
});


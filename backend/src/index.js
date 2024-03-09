const config = require("./Bootstrap/config.js");
const express = require("express");
const bodyParser = require('body-parser')
var cors = require('cors')

const api1 = require("./Controllers/Api1Controller.js");
const api2 = require("./Controllers/Api1Controller.js");
// const websockets = require("./Controllers/WebsocketsController.js");

const app = express();
var expressWs = require('express-ws')(app);
app.use(bodyParser.json({limit: '50mb'}))
app.use(bodyParser.urlencoded({ extended: false }))
app.use(cors())

app.use("/api/v1", api1);
app.use("/api/v2", api2);

// app.use("/api/ws", websockets);
app.ws('/api/ws/stream', function(ws, req) {
        console.log("Websocket connection established");
        ws.on('message', function(msg) {
                console.log("Websocket connection doing");
                ws.send(msg);
        });
        ws.on('close', function() {
                console.log("Websocket connection closed");
        });
})

app.listen(config.port, () => {
        console.log(`Server is running on port http://localhost:${config.port}`);
})
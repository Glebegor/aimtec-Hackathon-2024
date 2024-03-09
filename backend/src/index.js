const config = require("./Presentation/Bootstrap/config.js");
const express = require("express");
const app = express();
const db = require("./Presentation/Bootstrap/db.js");
const router = require("./Presentation/Controllers/Controller.js").NewController().router;
app.get("/", (req, res) => {
    res.send("!!Hello world!!")
})
app.use(router) // Controller

app.listen(config.default.port, () => {
        console.log(`Server is running on port http://localhost:${config.default.port}`);
})
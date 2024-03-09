const env = require('dotenv').config({path: "./src/configs/.env"})
var config = require("../configs/dev.json");
config["database"]["password"] = env.parsed.DB_PASSWORD;

module.exports = config;
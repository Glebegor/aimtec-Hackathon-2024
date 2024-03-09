const express = require("express");

const WorkWTController = require('./WorkWTController.js')

const router = express.Router();

router.use('/workWT', WorkWTController)

module.exports = router;
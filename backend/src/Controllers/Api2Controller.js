const express = require("express");

const AuthWTController = require('./AuthController')

const router = express.Router();

router.use('/auth', AuthWTController)

module.exports = router;
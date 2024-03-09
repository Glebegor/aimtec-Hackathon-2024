const express = require('express')
const NeuralApi = "http://127.0.0.1:5000"

const router = express.Router();
router.post("/TextToSpeech", async (req,res) => {
  const { text, textLanguage, textToLanguage } = req.body;

  if (!text || !textLanguage || !textToLanguage) {
    res.status(400).json({"message": "Bad request"});
    return;
  }

  try {
    const response = await fetch(NeuralApi + "/workWT/TextToSpeech", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text, textLanguage, textToLanguage })
    });

    if (!response.ok) {
      res.status(500).json({"message": "Internal server error"});
      return;
    }

    const { speech, speechLanguage } = await response.json();

    console.log();

    res.status(200).json({speech: speech, speechLanguage: speechLanguage});
  } catch (error) {
    console.error("Error:", error.message);
    res.status(500).json({"message": "Internal server error"});
  }

});

router.post("/SpeechToText", async (req,res) => {
  const { speech, speechLanguage, speechToLanguage } = req.body;

  if (!speech || !speechLanguage || !speechToLanguage) {
    res.status(400).json({"message": "Bad request"});
    return;
  }

  try {
    const response = await fetch(NeuralApi + "/workWT/SpeechToText", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ speech, speechLanguage, speechToLanguage })
    });

    if (!response.ok) {
      res.status(500).json({"message": "Internal server error"});
      return;
    }

    const { text, textLanguage } = await response.json();


    res.status(200).json({ text:"text", textLanguage:"textLanguage" });
  } catch (error) {

    console.error("Error:", error.message);
    res.status(500).json({"message": "Internal server error"});
  }


});

module.exports = router;
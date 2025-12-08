// server.js - Node.js version of MediScan AI (optional)
const express = require('express');
const multer = require('multer');
const app = express();
const upload = multer();

app.use(express.static('public'));

app.get('/', (req, res) => {
  res.send(`
    <h1 style="text-align:center; color:#e74c3c; margin-top:100px">
      MediScan AI by Prit Bhatt
    </h1>
    <p style="text-align:center; font-size:24px">
      Fake Medicine Detector • 11th Grade Project • Ahmedabad
    </p>
  `);
});

app.post('/scan', upload.single('image'), (req, res) => {
  // Mock response (real ML will go here)
  res.json({
    drug_name: "Paracetamol 650mg",
    expiry: "2027",
    is_fake: false,
    confidence: 98.7,
    message: "Genuine Medicine - Safe to use"
  });
});

app.listen(3000, () => {
  console.log("MediScan AI Node.js server running on http://localhost:3000");
  console.log("By Prit Kalpesh Kumar Bhatt - 11th Grade");
});
const express = require('express');
const path = require('path');
const app = express();
app.use(express.urlencoded({ extended: false }));

app.get('/login', (req, res) => {
  res.sendFile(path.join(__dirname, 'static/login.html'));
});

app.post('/login', (req, res) => {
  // Dummy authentication
  res.redirect('/dashboard');
});

app.get('/dashboard', (req, res) => {
  res.send('<h1>Dashboard</h1>');
});

app.listen(3000, () => {
  console.log('Server listening on port 3000');
});

const express = require('express');
const bodyParser = require('body-parser');
const db = require('./db'); 

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));

app.post('/submit', async (req, res) => {
    const { first_name, last_name } = req.body;

    const existing = await db.checkName(first_name, last_name);
    if (existing) {
        return res.send('Name already exists <a href="/">Try again</a>');
    }

    await db.addName(first_name, last_name);
    res.send(`Name added! <a href="/">Go back</a>`);
});

app.listen(80, () => {
    console.log('Service B running on port 80');
});

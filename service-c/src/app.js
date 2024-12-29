const express = require('express');
const db = require('./db');

const app = express();

app.get('/', async (req, res) => {
    const users = await db.getAllNames();
    res.render('index', { users });
});

app.get('/delete/:id', async (req, res) => {
    await db.deleteName(req.params.id);
    res.redirect('/');
});

app.listen(81, () => {
    console.log('Service C running on port 81');
});

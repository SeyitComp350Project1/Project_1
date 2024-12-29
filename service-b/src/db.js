const { Client } = require('pg');
const client = new Client({
    connectionString: process.env.DATABASE_URL
});
client.connect();

const checkName = async (first_name, last_name) => {
    const result = await client.query(
        'SELECT * FROM users WHERE first_name = $1 AND last_name = $2',
        [first_name, last_name]
    );
    return result.rows.length > 0;
};

const addName = async (first_name, last_name) => {
    const timestamp = new Date().toISOString();
    await client.query(
        'INSERT INTO users (first_name, last_name, created_at) VALUES ($1, $2, $3)',
        [first_name, last_name, timestamp]
    );
};

module.exports = { checkName, addName };

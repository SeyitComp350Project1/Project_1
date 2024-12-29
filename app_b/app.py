from flask import Flask, request, render_template_string
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

connection = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        cur = connection.cursor()
        cur.execute("SELECT * FROM names WHERE first_name=%s AND last_name=%s", (first_name, last_name))
        if cur.fetchone():
            return "Name already exists. <a href='/'>Enter a new name</a>"
        else:
            cur.execute("INSERT INTO names (first_name, last_name) VALUES (%s, %s)", (first_name, last_name))
            connection.commit()
            cur.execute("SELECT COUNT(*) FROM names")
            count = cur.fetchone()[0]
            return f"Record added. Total records: {count}. <a href='/'>Enter a new name</a>"
    return '''
        <form method="post">
            First Name: <input type="text" name="first_name"><br>
            Last Name: <input type="text" name="last_name"><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0')

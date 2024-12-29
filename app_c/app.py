from flask import Flask, render_template_string, redirect, request
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

@app.route('/')
def index():
    cur = connection.cursor()
    cur.execute("SELECT * FROM names")
    rows = cur.fetchall()
    html = "<ul>"
    for row in rows:
        html += f"<li>{row[0]} - {row[1]} {row[2]} ({row[3]}) <a href='/delete/{row[0]}'>x</a></li>"
    html += "</ul><a href='/'>Refresh</a>"
    return html

@app.route('/delete/<int:id>')
def delete(id):
    cur = connection.cursor()
    cur.execute("DELETE FROM names WHERE id=%s", (id,))
    connection.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

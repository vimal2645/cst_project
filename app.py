from flask import Flask, render_template, request, redirect
import sqlite3
import os

#  Tell Flask exactly where to find templates and static files
app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

#  Initialize the database
def init_db():
    if not os.path.exists("app/database.db"):
        os.makedirs("app", exist_ok=True)
        conn = sqlite3.connect("app/database.db")
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                message TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

#  Home page
@app.route('/')
def index():
    return render_template('index.html')

#  Form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']

    conn = sqlite3.connect("app/database.db")
    c = conn.cursor()
    c.execute("INSERT INTO tickets (name, message) VALUES (?, ?)", (name, message))
    conn.commit()
    conn.close()
    return redirect('/tickets')

#  Show tickets
@app.route('/tickets')
def tickets():
    conn = sqlite3.connect("app/database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM tickets")
    tickets = c.fetchall()
    conn.close()
    return render_template('tickets.html', tickets=tickets)

#  Run app
if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)

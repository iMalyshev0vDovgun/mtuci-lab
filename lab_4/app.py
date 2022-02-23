from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    database = "service_db",
    user = "postgres",
    password = "",
    host = "localhost",
    port = "5432"
)

cursor = conn.cursor()


@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')


@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if "".__eq__(username.strip()) or "".__eq__(password.strip()):
        return render_template('error.html', error = 1)

    cursor.execute(
        "SELECT * FROM service.users WHERE login=%s AND password=%s",
        (str(username), str(password))
    )
    records = list(cursor.fetchall())

    if records.__len__() == 0:
        return render_template('error.html', error = 2)

    return render_template('account.html', data = records)
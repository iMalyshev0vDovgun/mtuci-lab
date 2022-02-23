from flask import Flask, render_template, request, redirect
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


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':

        if request.form.get("login"):

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

        elif request.form.get("registration"):

            return redirect("/registration/")

    return render_template('login.html')


@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':

        name = request.form.get('name')
        user_login = request.form.get('login')
        password = request.form.get('password')

        if ("".__eq__(name.strip()) or
                "".__eq__(user_login.strip()) or
                "".__eq__(password.strip())):
            return render_template('error.html', error = 1)

        cursor.execute(
            "SELECT * FROM service.users WHERE login=%s AND password=%s",
            (str(user_login), str(password))
        )
        records = list(cursor.fetchall())

        if records.__len__() != 0:
            return render_template('error.html', error = 3)

        cursor.execute(
            "INSERT INTO service.users (full_name, login, password) VALUES (%s, %s, %s);",
            (str(name), str(user_login), str(password))
        )

        conn.commit()
        return redirect('/login/')

    return render_template('registration.html')
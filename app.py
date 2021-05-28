from flask import Flask,render_template, request
import flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'eu-cdbr-west-01.cleardb.com'
app.config['MYSQL_USER'] = 'b6a158ec9d69b9'
app.config['MYSQL_PASSWORD'] = '8db978d9'
app.config['MYSQL_DB'] = 'heroku_a8e7065117af1c6'

mysql = MySQL(app)

@app.route("/")
def form():
    return render_template('/templates/form.html')

@app.route('/login', methods = ['POST','GET'])
def login():
    if request.method == 'GET':
        return "Please follow to /form page"
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['pwd']

        if(username != " " and password != " "):
            query = mysql.connection.cursor()
            query.execute("SELECT username, password FROM Login WHERE username = %s AND password = %s", (username, password))
            
            account = query.fetchone()
            
            if account:
                return 'Login in succesfully'
            else:
                return 'incorrect login'

if __name__ == "__main__":
    app.run()

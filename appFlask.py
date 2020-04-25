from flask import Flask, render_template, request, redirect, url_for
import mysql.connector


taskdb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="taskapp"
)

app = Flask(__name__)

@app.route('/')  # BackSlash Home o página principal
def index():
    sql = "SELECT * FROM app"
    cursor = taskdb.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return render_template('index.html', tasks = result)

@app.route('/createtask')
def create():
    return render_template('create-task.html')

@app.route('/addtask', methods={'POST'})
def addtask():
    if request.method == 'POST':
        taskname = request.form['taskName']
        taskdate = request.form['taskDate']
        cursor = taskdb.cursor()
        sql = f"INSERT INTO app (task,date) VALUES ('{taskname}','{taskdate}')"
        cursor.execute(sql)
        taskdb.commit()
        return redirect(url_for('index'))
    return "Error"

if __name__== "__main__":
    app.run(debug=True) # Debug=True para que se actualice automatico

 
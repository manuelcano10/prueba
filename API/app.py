from flask import Flask, jsonify, request
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = ""
)

# http://
app = Flask(__name__)

@app.route('/read', methods = ['GET'])
def read():
    sql = "SELECT * FROM task"
    cur = mydb.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    return jsonify(tasks = result)

@app.route('/create', methods = ['POST'])
def create():
    data = request.get_json()
    task = data['task']
    date = data['date']
    if(task == "" or date == ""):
        return jsonify(response = "Bad format, Try again")
    else:
        sql = f"INSERT INTO tasks (task,date) VALUES('{task}','{date}')"
        cur = mydb.cursor()
        cur.execute(sql)
        mydb.commit()
        return jsonify(response = "Task Created succesfully")


@app.route('/update', methods = ['PUT'])
def update():
    data = request.get_json()
    id = data['id']
    task = data['task']
    date = data['date']
    if(id == ""):
        return jsonify(response = "Bad format, try again")
    else:
        sql = f"UPDATE tasks SET task = '{task}', date = '{date}' WHERE id = {id}"
        cur = mydb.cursor()
        cur.execute(sql)
        mydb.commit()
        return jsonify(response = "Task Update succesfully")


@app.route('/delete', methods = ['DELETE'])
def delete():
    data = request.get_json()
    id = data['id']
    if(id == ""):
        return jsonify(response = "Bad format, try again")
    else:
        sql = f"DELETE FROM tasks  WHERE id = {id}"
        cur = mydb.cursor()
        cur.execute(sql)
        mydb.commit()
        return jsonify(response = "Task Delete succesfully")





if __name__ == "__main__":
    app.run(debug=True)
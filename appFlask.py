from flask import Flask, render_template, request, redirect, url_for
import requests as req

app = Flask(__name__)

@app.route('/read')  
def home():
    response = req.get('http://localhost:3000/api/listtasks')
    result = response.json()['tasks']
    return render_template('home.html', tasks = result)

@app.route('/edit')
def edit():
    id = request.args.get('id')
    response = req.get(f'http://localhost:3000/api/gettask?id={id}')
    result = response.json()['task']
    return render_template('edit-task.html', task = result)

@app.route('/update', methods = ['POST'])
def update():
    id = request.args.get('id')
    task = request.form['taskName']
    date = request.form['taskDate']
    editData = {"id": id, "task": task, "date": date}
    response = req.put('http://localhost:3000/api/updatetask', json = editData)
    return redirect(url_for('read'))

@app.route('/delete')
def delete():
    id = request.args.get('id')
    deleteData = {"id": id}
    response = req.delete('http://localhost:3000/api/deletetask', json = deleteData)
    return redirect(url_for('read'))

@app.route('/createtask')
def create():
    return render_template('create-task.html')

@app.route('/addtask', methods={'POST'})
def addtask():
    task = request.form['taskName']
    date = request.form['taskDate']
    addTask = {"task":task, "date": date}
    response = req.post('http://localhost:3000/api/addtask')
    return redirect(url_for('index'))


if __name__== "__main__":
    app.run(debug=True) # Debug=True para que se actualice automatico

 
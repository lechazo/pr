from flask import Flask, render_template, request
import MySQLdb

app = Flask(__name__)

db = MySQLdb.connect(host="localhost", user="root", passwd="zwx123.", db="db_test")

cursor = db.cursor()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", (name, age))
        db.commit()
        return "Record added successfully"

@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        id = request.form['id']
        cursor.execute("DELETE FROM students WHERE id = %s", (id,))
        db.commit()
        return "Record deleted successfully"

@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        age = request.form['age']
        cursor.execute("UPDATE students SET name=%s, age=%s WHERE id=%s", (name, age, id))
        db.commit()
        return "Record updated successfully"

@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        name = request.form['name']
        cursor.execute("SELECT * FROM students WHERE name = %s", (name,))
        results = cursor.fetchall()
        return render_template('search_results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)

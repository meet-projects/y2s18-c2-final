# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

# Add functions you need from databases.py to the next line!
from databases import add_student, get_all_students

# Starting the flask app
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

# App routing code here
@app.route('/register_student')
def register_student():
    return render_template('register_student.html')

<<<<<<< HEAD
@app.route('/register_employer')
def register_employer():
    return render_template('register_employeer.html')
=======
@app.route('/register_employeer')
def register_employeer():
    return render_template('register_employee.html')
>>>>>>> 73b206629f85d061402079082a5eb7a3ea008760

@app.route('/login')
def login():
    return render_template('login.html')

<<<<<<< HEAD
=======
@app.route('/logedin')
def logedin():
    return render_template('home2.html')
>>>>>>> 73b206629f85d061402079082a5eb7a3ea008760

# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)

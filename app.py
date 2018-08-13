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
def register():
    return render_template('register_student.html')

@app.route('/register_employeer')
def register():
    return render_template('register_employeer.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('')

# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)

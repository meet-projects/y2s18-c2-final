# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

# Add functions you need from databases.py to the next line!
from databases import add_student, get_all_students,check_log_in, add_job

# Starting the flask app
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

# App routing code here
@app.route('/register_student')
def register_student():
    return render_template('register_student.html')

@app.route('/register_employeer')
def register_employeer():
if request.method=get:
    return render_template('register_employee.html')
    eles:
        name= request.form["first name"
        password=request.form["pwd"]
        chack_password=request.form["check_pwd"]
        email=request.form["Email"]
        location=request.form["Location"]
        min_age=request.form["min_age"]
        salary]request.form["salary"]
        add_workplace{name,password,chak_password,email,location,min_age,salary)
        return redirect(url_4for"profale"_
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        students_email=request.form["Email"]
        students_password=request.form["password"]
        checking=check_log_in(students_email,students_password)
        if checking == None:
            return render_template('home.html', error = "retry password")
        else:
            session["logedin"]=True
            return redirect(url_for('jobspage'))
    return render_template('home.html')

@app.route('/jobspage')
def jobspage():
    if session.get("logedin") == True:
        return render_template('home2.html')
    else:
        return redirect(url_for("login"))

@app.route('/addjob')
def add_job_route():
    job_name=request.form["name"]
    job_desc=request.form["desc"]
    job_salary=request.form["salary"]
    job_location=request.form["location"]
    job_min_age=request.form["min_age"]
    add_job(job_name,job_desc,job_salary,job_location,job_min_age)
    return redirect(url_for("jobspage"))

@app.route('/profile')
def profile():
    return render_template('profile.html')
# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)

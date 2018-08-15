# Database related imports
# Make sure to import your tables!
import datetime 
from model import Base, Student_info, Workplace_info, Job

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Student_info,Workplace_info 
# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Your database functions are located under here (querying, adding items, etc.)
def add_job(name,desc,salary,location,min_age):
    job = Job(name=name, description=desc, salary=salary, location=location, min_age_jobs=min_age)
    session.add(job)
    session.commit()

def get_job():
    jobs = session.query(Job).all()
    return jobs

def add_student(user_name, password, full_name, birthday, email):
    student=Student_info(user_name=user_name, password=password, birthday=birthday, full_name=full_name, email=email)
    session.add(student)
    session.commit()

def add_workplace(name, password, email, location, min_age, salary):
    workplace=Workplace_info(workplace_password=password,
                             workplace_name=name, workplace_location=location, workplace_email=email,
                             min_age=min_age, salary=salary)
    session.add(workplace)
    session.commit()

def check_log_in(email, password):
    return  session.query(Student_info).filter_by(password=password, email=email).first()

def check_login_workplace(email, password):
    return session.query(Workplace_info).filter_by(workplace_email=email, workplace_password=password)

def get_all_students():
    students = session.query(Student_info).all()
    return students
    

# add_student("hasan", "hassan1", "hassan salah", datetime.date(1999,8,21), "hassan1@hotmail.com")
#add_student("alex", "alexx", "alex zoubi", datetime.date(2001,7,26), "alex2001@gmail.com")

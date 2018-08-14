# Database related imports
# Make sure to import your tables!
from model import Base, Student

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Student_info
from model import Base, Workplace_info 
# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Your database functions are located under here (querying, adding items, etc.)
def add_student(user_name,password,confirm_password,full_name,birthday,email):
    student=Student_info(user_name=user_name,password=password,confirm_password=confirm_password,full_name=full_name,birthday=birthday,email=email)
    session.add(student)
    session.commit()

def add_workplace(password,confirm_password,name,location,email,min_age,salary):
    workplace=Workplace_info(workplace_password=password,workplace_confirm_password=confirm_password,workplace_name=name,workplace_location=location,workplace_email=email,min_age=minage,salary=salary)
    session.add(workplace)
    session.commit()

def check_log_in(email, password):
    return  session.query(Student_info).filter_by(password=password, email=email).first()

def check_login_workplace(email, password):
    return session.query(Student_info).filter_by(workplace_email=email,workplace_password=password)

# Example of adding a student:
def add_student(student_name, student_year):
    print("Added a student!")
    student = Student(name=student_name, year=student_year)
    sekkssion.add(student)
    session.commit()

def get_all_students():
    students = session.query(Student).all()
    return students

# Database related imports
# Make sure to import your tables!
from model import Base, Student

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
grom model import base, Student_info
from model import base, Workplace_info 
# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Your database functions are located under here (querying, adding items, etc.)
def chek_log_in()
    students_info=session.query(Student_info).filter_by.{email=email).first
    if  request.format[password]=
# Example of adding a student:
def add_student(student_name, student_year):
    print("Added a student!")
    student = Student(name=student_name, year=student_year)
    session.add(student)
    session.commit()

def get_all_students():
    students = session.query(Student).all()
    return students

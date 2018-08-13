from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
class Student_info(base)
    __tablename__="student_info"
    user_number=Column(Integer,primary_key=true)
    user_name=Column(String)
    password=Column(Integer)
    confirm_password=Column(Integer)
    full_name=Column(String)
    birthday=Column(date)
    gender=Column(0
    email=Column(String)

class `Workplace_info(base) 
    __tablename__="workplace_info"
    user_number=Column(Integer,primary_key=true)
    workplace_password=Column(Integer)
    confirm_password=Column(Integer
    workplace_name=Column(String)
    workplace_location=Column(String)
    min_age=Column(Integer)
    workplace_email=Column(String)
    salary=Column(Integer)

# Example code:
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    year = Column(Integer)
    gender = Column(String)
    def __repr__(self):
        return ("Student name: {}, Student year:{}".format(self.name, self.year))

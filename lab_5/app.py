from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.comfig["SQLALCHEMY_DATABASE_URL"] = "sqlite://database.sqlite3"
db = SQLAlchemy(app)

class Student (db. Model):
    __tablename_ = 'student'
    Student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    roll_number = db.Column(db.String(200), nullable=False)
    first_name = db.Column(db.String(200), nullable=False, unique=True)
    last_name = db. Column (db. String (200))

class Course(db. Model):
    course = {"course_1" : 1, "course_2" : 2, "course_3" :3, "course_4":4}
    course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_code = db.Column(db.String(200), unique=True, nullable=False)
    course_name = db. Column(db. String(200), nullable=False)
    course_description = db. Column(db.String(200), unique=True, autoincrement=True)

class Enrollements(db.Model):
    Enrollement_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    estudent_id = db.Column(db.String, db.ForeignKey('student.student_id'), nullable=False)
    ecourse_id = db.Column(db.Integer, db.Foreignkey('course.course_id'), nullable=True)

    
def seed_course():
    c1 = Course(course_code = "CSE01", course_name = "MAD I", course_description ="Modern Apllication Development Course")
    c2 = Course(course_code = 'CSE02', course_name = "DBMS", course_description = "Database Management Systems")
    c3 = Course(course_code = "CSE03", course_name = "PDSA", course_description = "Programming Data Structures and algorithms using Python")
    c4 = Course(course_code = "CSE04", course_name = "BDM", course_description = "Business Data Management")
    db.session.add_all([c1, c2, c3, c4])
    db.session commit()
    

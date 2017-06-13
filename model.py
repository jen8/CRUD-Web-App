from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()



class Courses(db.Model):
    """Student Courses"""

    __tablename__ = 'courses'
    # foreign key established to brand table to link tables together
    # if a table that has a single matching row in the second table, 
    # the first table has foreign key
    course_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    course_name = db.Column(db.String(50), nullable=False)
    instructor_name = db.Column(db.String(50), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id')
    student = db.relationship('Student', backref='courses')

   

      

class Student(db.Model):
    """Students"""

    __tablename__ = 'students'
    student_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    grade_point_average = db.Column(db.Float, nullable=False)
    grade_level = db.Column(db.Integer, nullable=False)





##############################################################################
# Helper functions

def connect_to_db(app, db_uri=None):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    #app.config['SQLALCHEMY_DATABASE_URI'] = db_uri or 'postgresql:///crime'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri or 'postgres:///crime'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
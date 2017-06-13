import os


from jinja2 import StrictUndefined

from flask import Flask, send_from_directory, Request, render_template, request, flash, redirect, session, url_for
from flask_debugtoolbar import DebugToolbarExtension
from flask_restful import Resource Api
from werkzeug.utils import secure_filename




UPLOAD_FOLDER = './static/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


from model import connect_to_db, db, Courses, Student


app = Flask(__name__)
api = Api(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Required to use Flask sessions and the debug toolbar
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", "abcdef")

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True




@app.route('/', methods=['GET'])
def login_form():
    """Show school welcome page."""

    return render_template("home.html")


@app.route('/create', methods=['GET'])
def create():
    """Create Student"""

    return redirect("create.html")

@app.route('/process_registration', methods=['POST'])
def process_registration():
    """Takes student info from website and adds them to student database."""

    # take the student info
    
    first_name = request.form["firstname"]
    last_name = request.form["lastname"]
    gpa = request.form["gpa"]
    grade_level = request.form["gradelevel"]

    # take all of the student input and put all student info into database
    new_student = Student(first_name=firstname, 
    last_name=lastname, gpa = gpa, grade_level = gradelevel)

    db.session.add(new_student)

    # db.session.add(new_post)
    db.session.commit()


    
    flash("Student %s added." % firstname)

    
    return render_template("make_post.html")
 

@app.route('/delete', methods=['GET'])
def delete():
    """Delete student record"""
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    flash("Student %s deleted." % firstname)

@app.route('/view', methods=['GET'])
def view():
    """View all student records"""
    student_record = Student.query.all()s



  

if __name__ == "__main__":
    # app.run(debug=True)
    connect_to_db(app, os.environ.get("DATABASE_URL"))
    #db.create_all()
    db.create_all(app=app)

    
    DEBUG = "NO_DEBUG" not in os.environ
    PORT = int(os.environ.get("PORT", 5000))

    #app.run(host="0.0.0.0", port=PORT, debug=debug)
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
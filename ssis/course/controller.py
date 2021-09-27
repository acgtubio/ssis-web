from . import courseBP
from flask import render_template
from ssis.models.CourseModel import Course
from ssis.models.CourseRepo import CourseRepo

@courseBP.route('/courses')
def course():
    data = CourseRepo.All()
    return render_template('course/courseList.html', data = data)

@courseBP.route('/courses/add')
def courseAdd():
    return 'add course here'
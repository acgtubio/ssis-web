from . import courseBP
from flask import render_template, jsonify, redirect, request
from ssis.models.CourseModel import Course
from ssis.models.CourseRepo import CourseRepo
from ssis.controllers.course.CourseForm import CourseForm

@courseBP.route('/courses')
def course():
    keyword = request.args.get('keyword', '', type=str)
    data = CourseRepo.Search(keyword)
    return render_template('course/courseList.html', data = data)

@courseBP.route('/courses/add', methods=['GET'])
def courseAddRender():
    form = CourseForm()

    return render_template('course/course.html', form=form, title='Add Course', ac='.courseAdd')

@courseBP.route('/courses/add', methods=['POST'])
def courseAdd():
    form = CourseForm(form=request.form)

    if form.validate():
        course = Course(form.course_code.data, form.course_name.data, form.college_id.data)
        CourseRepo.Add(course)

        return redirect('/courses')
    return render_template('course/course.html', form=form, title='Add Course', ac='.courseAdd')

@courseBP.route('/courses/edit', methods=['GET'])
def courseEditRender():
    cc = request.args.get('id')
    course = CourseRepo.getByID(cc)

    form = CourseForm(course=course)

    return render_template('course/course.html', form=form, title="Edit Course", ac='.courseEdit')

@courseBP.route('/courses/edit', methods=['POST'])
def courseEdit():
    form = CourseForm(form=request.form, editInfo=True)

    if form.validate():
        course = Course(form.course_code.data, form.course_name.data, form.college_id.data)
        a = CourseRepo.Update(course)
        print(a)

        return redirect('/courses')
    return render_template('course/course.html', form=form, title='Edit Course', ac='.courseEdit')

@courseBP.route('/api/deleteCourse', methods=['POST'])
def deleteCourse():
    cc = request.form['id']
    res = CourseRepo.Delete(cc)

    return jsonify(success=res)
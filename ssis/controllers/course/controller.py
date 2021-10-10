from . import courseBP
from flask import render_template, jsonify, redirect, request, url_for
from ssis.models.CourseModel import Course
from ssis.models.CourseRepo import CourseRepo
from ssis.controllers.course.CourseForm import CourseForm
import math

@courseBP.route('/courses')
def course():
    keyword = request.args.get('keyword', '', type=str)
    page = request.args.get('page', 1, type=int)

    data = CourseRepo.Search(keyword, page, 10)
    courseCount = CourseRepo.Count(keyword)

    pages = []
    pageCount = math.ceil(courseCount/10)
    
    for x in range(page-5, page+6):
        if x >=1 and x<=pageCount:
            pages.append((x, url_for('.course', page=x, keyword=keyword)))

    prev = url_for('.course', page=page-1, keyword=keyword) if page > 1 else None
    nxt = url_for('.course', page=page+1, keyword=keyword) if page < pageCount else None

    return render_template('course/courseList.html', data = data, prev=prev, nxt=nxt, currPage=page, pages=pages)

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
from flask import render_template, jsonify, request, redirect, url_for
from . import studentBP
from ssis.models.StudentModel import Student
from ssis.models.StudentRepo import StudentRepo
from ssis.controllers.student.forms import StudentForm
from ssis.cloudinary.cloudinary import Cloudinary
from io import BufferedReader
import math

default_studentImgUrl = "https://res.cloudinary.com/dhb9d15rg/image/upload/v1637661391/SeekPng.com_profile-icon-png_9665317_yi4d3t.png"

@studentBP.route('/students', methods=['GET'])
@studentBP.route('/')
def students():
    keyword = request.args.get('keyword', '', str)
    page = request.args.get('page', 1, int)

    st = StudentRepo.Search(keyword, page, 10)
    stc = StudentRepo.Count(keyword)

    pages = []
    pageCount = math.ceil(stc/10)
    
    for x in range(page-5, page+6):
        if x >=1 and x<=pageCount:
            pages.append((x, url_for('.students', page=x, keyword=keyword)))

    prev = url_for('.students', page=page-1, keyword=keyword) if page > 1 else None
    nxt = url_for('.students', page=page+1, keyword=keyword) if page < pageCount else None

    return render_template('/student/studentList.html', title="Student List", students=st, prev=prev, nxt=nxt, currPage = page, pages=pages)

@studentBP.route('/students/add', methods=['GET'])
def studentAddRender():
    f = StudentForm()
    return render_template('/student/addStudent.html', title="Add Student", form=f, ac='.studentAdd')

@studentBP.route('/students/add', methods=['POST'])
def studentAdd():
    form = StudentForm()
    # stPhoto = request.files.get('photo', None)
    stPhoto = request.files['photo']
    # stPhoto = BufferedReader(stPhoto)

    if form.gender.data != 'others':
        form.customGender.data = form.gender.data

    if form.validate() :
        cldn = Cloudinary()
        if stPhoto:
            res = cldn.uploadImage(stPhoto, form.studentID.data)

        if res['status_code'] == 200:
            student = Student(form.studentID.data, form.firstname.data.capitalize(), form.lastname.data.capitalize(), form.course.data, form.year.data, form.customGender.data.capitalize(), res['image_url'])
            b = StudentRepo.Add(student)

        return redirect('/')

    form.customGender.data = ''
    return render_template('/student/addStudent.html', title="Add Student", form=form, ac='.studentAdd')

@studentBP.route('/students/edit', methods=['GET'])
def studentEditRender():
    k = request.args.get('id')
    st = StudentRepo.getByID(k)

    url = st.imgUrl if st.imgUrl else default_studentImgUrl
    f = StudentForm(st)

    return render_template('/student/addStudent.html', title="Edit Student", form=f, ac='.studentEdit', url=url)

@studentBP.route('/students/edit', methods=['POST'])
def studentEdit():
    form = StudentForm(form = request.form, editInfo=True)
    stPhoto = request.files['photo']

    if form.gender.data != 'others':
        form.customGender.data = form.gender.data

    if form.validate():
        cldn = Cloudinary()
        if stPhoto:
            res = cldn.uploadImage(stPhoto, form.studentID.data)

        if res['status_code'] == 200:
            student = Student(form.studentID.data, form.firstname.data.capitalize(), form.lastname.data.capitalize(), form.course.data, form.year.data, form.customGender.data.capitalize(), res['image_url'])
            StudentRepo.Update(student)
        
        return redirect('/')
    
    if form.gender != 'others':
        form.customGender.data = ''
    return render_template('/student/addStudent.html', title="Edit Student", form=form, ac='.studentEdit')

@studentBP.route('/api/deleteStudent', methods=['POST'])
def deleteStudent():
    studentID = request.form['id']
    res = StudentRepo.Delete(studentID)
    cldn = Cloudinary()
    a = cldn.removeImg(studentID)
    return jsonify(success=res)
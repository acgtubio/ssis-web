from flask import render_template, jsonify, request, redirect
from . import studentBP
from ssis.models.StudentModel import Student
from ssis.models.StudentRepo import StudentRepo
from ssis.controllers.student.forms import StudentForm
from ssis.models.SearchForm import SearchForm

@studentBP.route('/students', methods=['GET'])
@studentBP.route('/')
def students():
    keyword = request.args.get('keyword', '', str)
    page = request.args.get('page', '1', int)
    st = StudentRepo.Search(keyword)

    return render_template('/student/studentList.html', title="Student List", students=st)

@studentBP.route('/students/add', methods=['GET'])
def studentAddRender():
    f = StudentForm()
    return render_template('/student/addStudent.html', title="Add Student", form=f, ac='.studentAdd')

@studentBP.route('/students/add', methods=['POST'])
def studentAdd():
    form = StudentForm(form = request.form)
    if form.gender != 'others':
        form.customGender.data = form.gender.data

    if form.validate() :
        student = Student(form.studentID.data, form.firstname.data, form.lastname.data, form.course.data, form.year.data, form.customGender.data)
        StudentRepo.Add(student)
        return redirect('/')

    form.customGender.data = ''
    return render_template('/student/addStudent.html', title="Add Student", form=form, ac='.studentAdd')

@studentBP.route('/students/edit', methods=['GET'])
def studentEditRender():
    k = request.args.get('id')
    st = StudentRepo.getByID(k)
    f = StudentForm(st)

    return render_template('/student/addStudent.html', title="Edit Student", form=f, ac='.studentEdit')

@studentBP.route('/students/edit', methods=['POST'])
def studentEdit():
    form = StudentForm(form = request.form, editInfo=True)
    
    if form.gender != 'others':
        form.customGender.data = form.gender.data

    if form.validate():
        student = Student(form.studentID.data, form.firstname.data, form.lastname.data, form.course.data, form.year.data, form.customGender.data)
        StudentRepo.Update(student)
        return redirect('/')
    
    if form.gender != 'others':
        form.customGender.data = ''
    return render_template('/student/addStudent.html', title="Edit Student", form=form, ac='.studentEdit')

# @studentBP.route('/students/searchStudent', methods=["GET"])
# def getStudent():
#     k = request.args.get('keyword')
#     st = StudentRepo.Search(k)
#     return render_template('/student/')

@studentBP.route('/api/deleteStudent', methods=['POST'])
def deleteStudent():
    studentID = request.form['id']
    res = StudentRepo.Delete(studentID)
    return jsonify(success=res)
from flask import render_template, jsonify
from . import studentBP
from ssis.models.StudentModel import Student
from ssis.models.StudentRepo import StudentRepo

@studentBP.route('/students')
def students():
    st = StudentRepo.All()
    return render_template('/student/studentList.html', title="Student List", students=st)
    # return 'wow'

@studentBP.route('/students/add', methods=['POST', 'GET'])
def studentAdd():
    # st = Student('2019-0094', 'Adrian Christopher', 'Tubio', 'BSCS', '3', 'Male')
    # res =  StudentRepo.Add(st)
    return 'hey'

@studentBP.route('/api/students')
def getStudent():
    st = StudentRepo.All()
    return jsonify(id=st[0].id)
    # return 'wow'
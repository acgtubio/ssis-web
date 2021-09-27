from . import collegeBP
from flask import render_template
from ssis.models.CollegeModel import College
from ssis.models.CollegeRepo import CollegeRepo

@collegeBP.route('/colleges')
def college():
    colleges = CollegeRepo.All()
    return render_template('/college/collegeList.html', data = colleges)

@collegeBP.route('/colleges/add')
def collegeAdd():
    return 'add college'
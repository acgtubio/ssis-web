from . import collegeBP
from flask import render_template, request, redirect, jsonify
from ssis.models.CollegeModel import College
from ssis.models.CollegeRepo import CollegeRepo
from ssis.controllers.college.CollegeForm import CollegeForm

@collegeBP.route('/colleges')
def college():
    keyword = request.args.get('keyword', '', type=str)
    colleges = CollegeRepo.Search(keyword)
    return render_template('/college/collegeList.html', data = colleges)

@collegeBP.route('/colleges/add', methods=['GET'])
def collegeAddRender():
    form = CollegeForm()

    return render_template('/college/college.html', title='Add College', ac='.collegeAdd', form=form)

@collegeBP.route('/colleges/add', methods=['POST'])
def collegeAdd():
    form = CollegeForm(form=request.form)

    if form.validate():
        college = College(form.college_code.data, form.college_name.data)
        CollegeRepo.Add(college)

        return redirect('/colleges')

    return render_template('/college/college.html', title='Add College', ac='.collegeAdd', form=form)

@collegeBP.route('/colleges/edit', methods=['GET'])
def collegeEditRender():
    code = request.args.get('college_code')
    college = CollegeRepo.getByID(code)
    form = CollegeForm(college=college)

    return render_template('/college/college.html', title='Edit College', ac='.collegeEdit', form=form)

@collegeBP.route('/colleges/edit', methods=['POST'])
def collegeEdit():
    form = CollegeForm(form=request.form, editInfo=True)

    if form.validate():
        college = College(form.college_code.data, form.college_name.data)
        CollegeRepo.Update(college)

        return redirect('/colleges')

    return render_template('/college/college.html', title='Edit College', ac='.collegeEdit', form=form)

@collegeBP.route('/api/deleteCollege', methods=['POST'])
def deleteCollege():
    code = request.form['id']
    res = CollegeRepo.Delete(code)

    return jsonify(success=res)

@collegeBP.route('/api/searchCollege', methods=['GET'])
def searchCollege():
    keyword = request.args.get('keyword')
    colleges = CollegeRepo.Search(keyword)

    return jsonify(colleges)

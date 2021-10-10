from . import collegeBP
from flask import render_template, request, redirect, jsonify, url_for
from ssis.models.CollegeModel import College
from ssis.models.CollegeRepo import CollegeRepo
from ssis.controllers.college.CollegeForm import CollegeForm
import math

@collegeBP.route('/colleges')
def college():
    keyword = request.args.get('keyword', '', type=str)
    page = request.args.get('page', 1, type=int)

    colleges = CollegeRepo.Search(keyword, page, 10)
    collegeCount = CollegeRepo.Count(keyword)

    pages = []
    pageCount = math.ceil(collegeCount/10)

    for x in range(page-5, page+6):
        if x >=1 and x<=pageCount:
            pages.append((x, url_for('.college', page=x, keyword=keyword)))

    prev = url_for('.college', page=page-1, keyword=keyword) if page > 1 else None
    nxt = url_for('.college', page=page+1, keyword=keyword) if page < pageCount else None

    return render_template('/college/collegeList.html', data = colleges, prev=prev, nxt=nxt, currPage=page, pages=pages)

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

from flask_wtf import FlaskForm
from ssis.models.CourseRepo import CourseRepo
from ssis.models.CollegeRepo import CollegeRepo
from wtforms import StringField, SubmitField, validators, SelectField

class CourseForm(FlaskForm):
    course_code = StringField('Course code', validators = [
        validators.DataRequired(),
    ])
    course_name = StringField('Course Name', [
        validators.DataRequired(),
        validators.Length(max=50)
    ])
    college_id = SelectField('College', validators=[validators.DataRequired()])

    submit = SubmitField("Submit")

    def validate_course_code(self, course_code):
        cc = CourseRepo.getByID(course_code.data)
        if cc and not self.edit:
            raise validators.ValidationError('Course code already taken.')
    

    def __init__(self, course = None, form = None, editInfo=False):
        super().__init__(form)
        self.edit = editInfo;
        colleges = []

        for college in CollegeRepo.All():
            colleges.append((college.id, college.college_name))
        
        self.college_id.choices = colleges


        if course:
            self.course_code.render_kw = {'readonly': ''}
            self.course_code.default = course.id
            self.course_name.default = course.course_name
            self.college_id.default = course.college_id
            self.process()           
            
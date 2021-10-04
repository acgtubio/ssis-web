from flask_wtf import FlaskForm
from ssis.models.CollegeRepo import CollegeRepo
from wtforms import StringField, SubmitField, validators

class CollegeForm(FlaskForm):
    college_code = StringField('College code', validators = [
        validators.DataRequired(),
    ])
    college_name = StringField('College Name', [
        validators.DataRequired(),
        validators.Length(max=50)
    ])
    submit = SubmitField("Submit")

    def validate_college_code(self, college_code):
        college_code = CollegeRepo.getByID(college_code.data)
        if college_code and not self.edit:
            raise validators.ValidationError('College code already taken.')
    

    def __init__(self, college = None, form = None, editInfo=False):
        super().__init__(form)
        self.edit = editInfo;

        if college:
            self.college_code.render_kw = {'readonly': ''}
            self.college_code.default = college.id
            self.college_name.default = college.college_name
            self.process()           
            
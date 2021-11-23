from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from ssis.models.CourseRepo import CourseRepo
from ssis.models.StudentRepo import StudentRepo
from wtforms import StringField, SubmitField, validators, SelectField, RadioField

class StudentForm(FlaskForm):
    photo = FileField('Image', validators=[
        FileRequired(),
        FileAllowed(['jpeg', 'jpg', 'png'], 'Images only!')
        ])

    studentID = StringField('Student ID', validators = [
        validators.DataRequired(),
        validators.Regexp('^\d\d\d\d-\d\d\d\d$')
    ])
    firstname = StringField('Firstname', [
        validators.DataRequired(),
        validators.Length(max=50)
    ])
    lastname = StringField('Lastname', [
        validators.DataRequired(),
        validators.Length(max=50)
    ])
    course = SelectField('Course', validators=[validators.DataRequired()])
    year = SelectField('Year', choices=[('1', '1st Year'), ('2', '2nd Year'), ('3', '3rd Year'), ('4', '4th Year')], validators=[validators.DataRequired()])
    gender = RadioField('Gender', choices=[('Male', 'Male'), ('Female', 'Female'), ('others', '')], validators=[validators.DataRequired()])
    customGender = StringField('Others, please specify', render_kw={'readonly': ''}, validators=[
        validators.DataRequired(),
        validators.Length(max=50)
    ])
    submit = SubmitField("Submit")

    def validate_studentID(self, studentID):
        studentID = StudentRepo.getByID(studentID.data)
        if studentID and not self.edit:
            raise validators.ValidationError('ID already taken.')
    

    def __init__(self, student = None, form = None, editInfo=False):
        super().__init__()
        courses = []
        for course in CourseRepo.All():
            courses.append((course.id, course.course_name))

        self.course.choices = courses
        self.edit = editInfo;

        if student:
            self.studentID.render_kw = {'readonly': ''}
            self.studentID.default = student.id
            self.firstname.default = student.firstname
            self.lastname.default = student.lastname
            self.year.default = student.year
            self.course.default = student.course

            if student.gender.casefold() == 'Male'.casefold() or student.gender.casefold() == "female".casefold():
                self.gender.default = student.gender.capitalize()
            else:
                self.gender.default = 'others'
                self.customGender.render_kw = {'enabled': ''}
                self.customGender.default = student.gender.capitalize()
            self.process()
            
            
from ssis.models.ModelJSON import ModelJSON
import json

class Student(ModelJSON):
    def __init__(self, idNo, firstname, lastname, course, year, gender, url):
        self.id = idNo
        self.firstname = firstname
        self.lastname = lastname
        self.course = course
        self.year = year
        self.gender = gender
        self.imgUrl = url

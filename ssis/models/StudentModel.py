import json

class Student():
    def __init__(self, idNo, firstname, lastname, course, year, gender):
        self.id = idNo
        self.firstname = firstname
        self.lastname = lastname
        self.course = course
        self.year = year
        self.gender = gender
    
    def toJSON(self):
        return json.dumps(self, default=lambda a: a.__dict__)

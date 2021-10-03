from ssis.models.ModelJSON import ModelJSON

class College(ModelJSON):
    def __init__(self, college_id, name):
        self.id = college_id
        self.college_name = name
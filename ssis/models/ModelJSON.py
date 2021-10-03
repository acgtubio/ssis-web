import json

class ModelJSON:
    def toJSON(self):
        return json.dumps(self, default=lambda a: a.__dict__)
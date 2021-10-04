from flask import Blueprint

studentBP = Blueprint('students', __name__)

from . import controller
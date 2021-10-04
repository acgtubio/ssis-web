from flask import Blueprint

courseBP = Blueprint('course', __name__)

from . import controller
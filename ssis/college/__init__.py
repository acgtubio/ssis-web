from flask import Blueprint

collegeBP = Blueprint('college', __name__)

from . import controller
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mysql_connector import MySQL
from config import DB_HOST, DB_NAME, DB_USER, DB_PASS

mysql = MySQL()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='wow',
        MYSQL_HOST=DB_HOST,
        MYSQL_DATABASE=DB_NAME,
        MYSQL_USER=DB_USER,
        MYSQL_PASSWORD=DB_PASS,
    )
    bootstrap = Bootstrap(app)
    mysql.init_app(app)

    @app.route('/')
    def hello():
        return 'hello'

    from .student import studentBP as stBP
    from .college import collegeBP as clgBP
    from .course import courseBP as crsBP

    app.register_blueprint(stBP)
    app.register_blueprint(clgBP)
    app.register_blueprint(crsBP)

    return app
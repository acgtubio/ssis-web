from ssis import mysql
from ssis.models.CourseModel import Course

class CourseRepo():
    @staticmethod
    def Add(course):
        cursor = mysql.connection.cursor()

        try:
            cursor.execute(f""" INSERT INTO course VALUES(
                '{course.id}', 
                '{course.course_name}',
                '{course.college_id}'
                )""")
        except Exception as e:
            return e

        mysql.connection.commit()
        return True
    
    @staticmethod
    def All():
        cursor = mysql.connection.cursor()
         
        try:
            cursor.execute(f"""
                SELECT * FROM course
            """)
            courses = cursor.fetchall()
        except Exception as e:
            return f'DINK DONK ERROR {e}'
        
        courseList = []
        for course in courses:
            co = Course(course[0], course[1], course[2])
            courseList.append(co)

        return courseList

    @staticmethod
    def Delete(id):
        cursor = mysql.connection.cursor()

        try:
            cursor.execute(f"""
                DELETE FROM course WHERE course_code = '{id}'
            """)
            mysql.connection.commit()
        except Exception as e:
            return f'{e}'
        
        return True
    
    @staticmethod
    def Update(course):
        cursor = mysql.connection.cursor()

        try:
            cursor.execute(f"""
                UPDATE course SET
                course_name = {course.course_name}
                WHERE course_code = {course.id}
            """)
            mysql.connection.commit()
        except Exception as e:
            return f'{e}'
        
        return True
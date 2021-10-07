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
                course_name = '{course.course_name}',
                college = '{course.college_id}'
                WHERE course_code = '{course.id}'
            """)
            mysql.connection.commit()
        except Exception as e:
            return f'{e}'
        
        return True
    
    @staticmethod
    def Search(keyword):
        cursor = mysql.connection.cursor()

        try:
            cursor.execute(f"""
                SELECT * FROM course
                WHERE course_code LIKE '%{keyword}%' OR
                course_name LIKE '%{keyword}%' OR
                college LIKE '%{keyword}%'
            """)
            courses = cursor.fetchall()
        except Exception as e:
            return f'{e}'
        
        courseJSON = []

        for course in courses:
            c = Course(course[0], course[1], course[2])
            courseJSON.append(c)

        return courseJSON

    @staticmethod
    def getByID(course_code):
        cursor = mysql.connection.cursor()

        try:
            cursor.execute(f"""
                SELECT * FROM course
                WHERE course_code = '{course_code}'
            """)
            course = cursor.fetchall()
        except Exception as e:
            return f'{e}'
        
        if course:
            c = Course(course[0][0], course[0][1], course[0][2])
            
            return c

        return False
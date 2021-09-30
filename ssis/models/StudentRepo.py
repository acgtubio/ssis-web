from ssis import mysql
from ssis.models.StudentModel import Student

class StudentRepo():
    @staticmethod
    def Add(student):
        cursor = mysql.connection.cursor()

        try:
            cursor.execute(f""" INSERT INTO student VALUES(
                '{student.id}', 
                '{student.firstname}', 
                '{student.lastname}', 
                '{student.course}', 
                '{student.year}', 
                '{student.gender}'
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
                SELECT * FROM student
            """)
            students = cursor.fetchall()
        except Exception as e:
            return f'DINK DONK ERROR {e}'
        
        studentList = []
        for student in students:
            st = Student(student[0], student[1], student[2], student[3], student[4], student[5])
            studentList.append(st)

        return studentList

    @staticmethod
    def Delete(id):
        cursor = mysql.connection.cursor()

        try:
            cursor.execute(f"""
                DELETE FROM student WHERE id = '{id}'
            """)
            mysql.connection.commit()
        except Exception as e:
            return f'{e}'
        
        return True
    
    @staticmethod
    def Update(student):
        cursor = mysql.connection.cursor()

        try:
            cursor.execute(f"""
                UPDATE student SET
                firstname = '{student.firstname}',
                lastname = '{student.lastname}',
                course = '{student.course}',
                yr = '{student.year}',
                gender = '{student.gender}'
                WHERE id = '{student.id}'
            """)
            mysql.connection.commit()
        except Exception as e:
            print(e)
            return f'{e}'
        
        return True

    @staticmethod
    def Search(keyword):
        cursor = mysql.connection.cursor()

        try:
            cursor.execute(f"""
                SELECT * FROM student
                WHERE id LIKE '%{keyword}%' OR
                firstname LIKE '%{keyword}%' OR
                lastname LIKE '%{keyword}%' OR
                course LIKE '%{keyword}%' OR
                yr LIKE '%{keyword}%' OR
                gender LIKE '%{keyword}%'
            """)
            st = cursor.fetchall()
        except Exception as e:
            return f"{e}"
        
        studentListInJSON = []

        for student in st:
            s = Student(student[0], student[1], student[2], student[3], student[4], student[5]).toJSON()
            studentListInJSON.append(s)

        return studentListInJSON
    
    @staticmethod
    def getByID(stID):
        cursor = mysql.connection.cursor()

        try:
            cursor.execute(f"""
                SELECT * FROM student
                WHERE id = '{stID}'
            """)
            st = cursor.fetchall()
        except Exception as e:
            return f"{e}"
        
        if st:
            student = Student(st[0][0], st[0][1], st[0][2], st[0][3], st[0][4] ,st[0][5])

            return student
        
        return False
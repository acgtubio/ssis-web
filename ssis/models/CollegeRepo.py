from ssis import mysql
from ssis.models.CollegeModel import College

class CollegeRepo():
    @staticmethod
    def Add(college):
        cursor = mysql.connection.cursor()

        try:
            cursor.execute(f""" INSERT INTO college VALUES(
                '{college.id}', 
                '{college.college_name}'
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
                SELECT * FROM college
            """)
            colleges = cursor.fetchall()
        except Exception as e:
            return f'DINK DONK ERROR {e}'
        
        collegeList = []
        for college in colleges:
            co = College(college[0], college[1])
            collegeList.append(co)

        return collegeList

    @staticmethod
    def Delete(id):
        cursor = mysql.connection.cursor()

        try:
            cursor.execute(f"""
                DELETE FROM college WHERE college_code = '{id}'
            """)
            mysql.connection.commit()
        except Exception as e:
            return f'{e}'
        
        return True
    
    @staticmethod
    def Update(college):
        cursor = mysql.connection.cursor()

        try:
            cursor.execute(f"""
                UPDATE college SET
                college_name = '{college.college_name}'
                WHERE college_code = '{college.id}'
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
                SELECT * FROM college
                WHERE college_code LIKE '%{keyword}%' OR
                college_name LIKE '%{keyword}%'
            """)
            colleges = cursor.fetchall()
        except Exception as e:
            return f'{e}'
        
        collegeJSON = []

        for college in colleges:
            c = College(college[0], college[1]).toJSON()
            collegeJSON.append(c)

        return collegeJSON

    @staticmethod
    def getByID(college_code):
        cursor = mysql.connection.cursor()

        try:
            cursor.execute(f"""
                SELECT * FROM college
                WHERE college_code = '{college_code}'
            """)
            college = cursor.fetchall()
        except Exception as e:
            return f'{e}'
        
        if college:
            c = College(college[0][0], college[0][1])
            
            return c

        return False
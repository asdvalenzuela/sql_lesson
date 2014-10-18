import sqlite3

DB = None
CONN = None

def make_new_student(first_name, last_name, github):
    query = """INSERT into Students values (?,?,?)"""
    DB.execute(query, (first_name,last_name,github))
    CONN.commit()
    return "Successfully added student: %s %s %s" % (first_name, last_name,github)

def make_new_project(title, max_grade):
    query = """INSERT into Projects (title, max_grade) values (?,?)"""
    DB.execute(query, (title, max_grade))
    CONN.commit()
    return "Successfully added project %s, with max grade %s" % (title, max_grade)



def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    return row
    # print row
#     return """\
# Student: %s %s
# Github account: %s"""%(row[0], row[1], row[2])

def get_projects_by_title(title):
    query = """SELECT title,description,max_grade FROM Projects WHERE title = ?"""
    DB.execute(query, (title,))
    row = DB.fetchone()
    # print row
    return """\
Project: %s
Description: %s 
Max_Grade: %s""" % (row[0], row[1], row[2]) 

def get_grade_by_project_title(student_github, project_title):
    # query = """SELECT first_name, last_name, 
    # project_title, grade FROM Grades JOIN Students ON 
    # (Students.github = Grades.student_github) WHERE project_title = ? AND student_github = ?"""
    # query = """SELECT first_name, last_name, 
    # project_title, grade FROM Grades, Students WHERE Grades.student_github = Students.github AND project_title = ? AND student_github = ?"""
    query = """SELECT student_name, student_github, project_title, grade FROM Grades WHERE student_github = ? AND project_title = ?"""
    DB.execute(query, (student_github,project_title,))
    row = DB.fetchone()
    # print 5.0, type(row)
    return """\
# Student Github: %s
# Project: %s 
Grade: %s""" % (row[0], row[1], row[2])

def get_grades_by_project_title(project_title):
    # query = """SELECT first_name, last_name, 
    # project_title, grade FROM Grades JOIN Students ON 
    # (Students.github = Grades.student_github) WHERE project_title = ? AND student_github = ?"""
    # query = """SELECT first_name, last_name, 
    # project_title, grade FROM Grades, Students WHERE Grades.student_github = Students.github AND project_title = ? AND student_github = ?"""
    query = """SELECT student_github, project_title, grade FROM Grades WHERE project_title = ?"""
    grades = {}
    for row in DB.execute(query, (project_title,)):
        grades[row[0]] = row[2]
    # print 5.0, type(row)
    return grades
    # return """\
# # Student Github: %s
# # Project: %s 
# Grade: %s""" % (row[0], row[1], row[2])

def give_grade(student_github,project_title,grade):
    #query = """UPDATE Grades SET grade = ? WHERE student_github = ? AND project_title = ?"""
    query = """INSERT into Grades values (?,?,?)"""
    DB.execute(query, (student_github,project_title,grade))
    CONN.commit()
    return "Successfully added grade %s to %s project for %s" % (grade,project_title,student_github)

def get_grades(student_github):
    query= """SELECT project_title, grade FROM Grades WHERE student_github = ?"""
    # print "Student Github: %s" %  student_github
    grade_list = {}
    for row in DB.execute(query, (student_github,)):
    # print DB.execute(query, (student_github))
        # row = DB.fetchone()
        grade_list[row[0]] = row[1]
    return grade_list
        # """\
# Student Github: %s        
# Project: %s
# Grade: %s""" % (row[0],row[1], row[2])

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()

def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        print 1.0, input_string
        tokens = input_string.split(",")
        print 2.0, tokens
        command = tokens[0]
        print 3.0, command
        args = tokens[1:]
        print 4.0, args

        if command == "student":
            get_student_by_github(*args) 
        if command == "new_student":
            make_new_student(*args)
        if command == "new_project":
            make_new_project(*args)
        if command == "project":
            get_projects_by_title(*args)
        if command == "grade":
            get_grade_by_project_title(*args)
        if command == 'give_grade':
            give_grade(*args)
        if command == "get_grades":
            get_grades(*args)    
        if command not in ["student", "new_student", "new_project", "project","grade","give_grade", "get_grades"]:
            continue

    CONN.close()

if __name__ == "__main__":
    main()

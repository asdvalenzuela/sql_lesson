import sqlite3

DB = None
CONN = None

def make_new_student(first_name, last_name, github):
    query = """INSERT into Students values (?,?,?)"""
    DB.execute(query, (first_name,last_name,github))
    CONN.commit()
    print "Successfully added student: %s %s" % (first_name, last_name)
#added this, not complete
def make_new_project(project_title, github):
    query = """INSERT into Students values (?,?,?)"""
    DB.execute(query, (first_name,last_name,github))
    CONN.commit()
    print "Successfully added student: %s %s" % (first_name, last_name)

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    print """\
Student: %s %s
Github account: %s"""%(row[0], row[1], row[2])
#added this, not complete
def get_projects_by_title(project_title):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    print """\
Project Title: %s %s
Github account: %s"""%(row[0], row[1], row[2])

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()

def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        # print 1.0, input_string
        tokens = input_string.split()
        # print 2.0, tokens
        command = tokens[0]
        # print 3.0, command
        args = tokens[1:]
        # print 4.0, args

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)

    CONN.close()

if __name__ == "__main__":
    main()

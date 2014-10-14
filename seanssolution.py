import sqlite3

DB = None
CONN = None

def connect_to_db():
    global DB, CONN

    CONN = sqlite3.connect("hb.db")
    DB = CONN.cursor()

def main():
    connect_to_db()

    query = "SELECT Students.first_name, Grades.project_title, Grades.grade FROM Students, Grades WHERE Students.github = Grades.student_github AND Students.first_name = ?"
    DB.execute(query, ("Sean",))
    row = DB.fetchone()
    print row

if __name__ == "__main__":
    main()
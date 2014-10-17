import hackbright_app
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/newstudent")
def new_student():
    return render_template("new_student.html")

@app.route("/projectgrades")
def get_projectgrades():
    hackbright_app.connect_to_db()
    project_name = request.args.get("project")
    row = hackbright_app.get_grades_by_project_title(project_name)
    html = render_template("new_student_record.html", project_title = project_name, project_grades = row)
    return html    

@app.route("/projectgrades")
def get_projectgrades():
    hackbright_app.connect_to_db()
    project_name = request.args.get("project")
    row = hackbright_app.get_grades_by_project_title(project_name)
    html = render_template("get_grades.html", project_title = project_name, project_grades = row)
    return html

@app.route("/student")
def get_student():
    hackbright_app.connect_to_db()
    student_github = request.args.get("github")
    row = hackbright_app.get_student_by_github(student_github)
    row2 = hackbright_app.get_grades(student_github)
    html = render_template("student_info.html", 
        first_name = row[0], last_name = row[1], github = row[2], grade = row2)
    return html

@app.route("/")
def get_github():
    return render_template("get_github.html")

if __name__ == "__main__":
    app.run(debug=True)
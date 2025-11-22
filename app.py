
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "university.db")

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return render_template("index.html")

# -------- Students --------
@app.route("/students")
def list_students():
    conn = get_db_connection()
    students = conn.execute("SELECT * FROM students ORDER BY last_name, first_name").fetchall()
    conn.close()
    return render_template("students.html", students=students)

@app.route("/students/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        major = request.form.get("major")
        level = request.form.get("level")
        enrollment_year = request.form.get("enrollment_year")

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO students (first_name, last_name, email, major, level, enrollment_year) VALUES (?, ?, ?, ?, ?, ?)",
            (first_name, last_name, email, major, level, enrollment_year),
        )
        conn.commit()
        conn.close()
        return redirect(url_for("list_students"))
    return render_template("add_student.html")

# -------- Courses --------
@app.route("/courses")
def list_courses():
    conn = get_db_connection()
    courses = conn.execute("SELECT * FROM courses ORDER BY course_code").fetchall()
    conn.close()
    return render_template("courses.html", courses=courses)

@app.route("/courses/add", methods=["GET", "POST"])
def add_course():
    if request.method == "POST":
        course_code = request.form["course_code"]
        title = request.form["title"]
        credits = request.form["credits"]
        department = request.form.get("department")

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO courses (course_code, title, credits, department) VALUES (?, ?, ?, ?)",
            (course_code, title, credits, department),
        )
        conn.commit()
        conn.close()
        return redirect(url_for("list_courses"))
    return render_template("add_course.html")

# -------- Faculty --------
@app.route("/faculty")
def list_faculty():
    conn = get_db_connection()
    faculty = conn.execute("SELECT * FROM faculty ORDER BY last_name, first_name").fetchall()
    conn.close()
    return render_template("faculty.html", faculty=faculty)

@app.route("/faculty/add", methods=["GET", 'POST'])
def add_faculty():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        department = request.form.get("department")

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO faculty (first_name, last_name, email, department) VALUES (?, ?, ?, ?)",
            (first_name, last_name, email, department),
        )
        conn.commit()
        conn.close()
        return redirect(url_for("list_faculty"))
    return render_template("add_faculty.html")

# -------- Enrollments --------
@app.route("/enrollments")
def list_enrollments():
    conn = get_db_connection()
    enrollments = conn.execute("""
        SELECT e.enrollment_id,
               s.first_name || ' ' || s.last_name AS student_name,
               c.course_code || ' - ' || c.title AS course_name,
               f.first_name || ' ' || f.last_name AS faculty_name,
               e.semester,
               e.year,
               e.grade
        FROM enrollments e
        JOIN students s ON e.student_id = s.student_id
        JOIN courses c  ON e.course_id = c.course_id
        LEFT JOIN faculty f ON e.faculty_id = f.faculty_id
        ORDER BY e.year DESC, e.semester, student_name
    """).fetchall()

    students = conn.execute("SELECT student_id, first_name || ' ' || last_name AS name FROM students ORDER BY name").fetchall()
    courses = conn.execute("SELECT course_id, course_code || ' - ' || title AS name FROM courses ORDER BY course_code").fetchall()
    faculty = conn.execute("SELECT faculty_id, first_name || ' ' || last_name AS name FROM faculty ORDER BY name").fetchall()
    conn.close()
    return render_template(
        "enrollments.html",
        enrollments=enrollments,
        students=students,
        courses=courses,
        faculty=faculty
    )

@app.route("/enrollments/add", methods=["POST"])
def add_enrollment():
    student_id = request.form["student_id"]
    course_id = request.form["course_id"]
    faculty_id = request.form.get("faculty_id") or None
    semester = request.form["semester"]
    year = request.form["year"]
    grade = request.form.get("grade")

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO enrollments (student_id, course_id, faculty_id, semester, year, grade) VALUES (?, ?, ?, ?, ?, ?)",
        (student_id, course_id, faculty_id, semester, year, grade),
    )
    conn.commit()
    conn.close()
    return redirect(url_for("list_enrollments"))

if __name__ == "__main__":
    app.run(debug=True)

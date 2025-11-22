University Course Registration System (Flask + SQLite)

This mini project is a web application to manage a university's academic catalog:
- Students
- Courses
- Faculty
- Enrollments

Folder contents
---------------
- app.py        : Python backend (Flask application)
- university.db : SQLite database with sample data
- schema.sql    : SQL script to recreate the database schema and sample data
- templates/    : Front-end HTML templates (Jinja2)

How to run
----------
1. Create and activate a virtual environment (optional but recommended).

2. Install required Python package:
   pip install flask

3. Make sure 'app.py' and 'university.db' are in the same folder.

4. Run the Flask app:
   python app.py

5. Open your browser and go to:
   http://127.0.0.1:5000/

You can:
- View and add Students, Courses, Faculty
- View and add Enrollments (linking students, courses, and faculty)

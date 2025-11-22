
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS faculty;

CREATE TABLE students (
    student_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name   TEXT NOT NULL,
    last_name    TEXT NOT NULL,
    email        TEXT UNIQUE NOT NULL,
    major        TEXT,
    level        TEXT, -- e.g., Undergraduate, Graduate
    enrollment_year INTEGER
);

CREATE TABLE courses (
    course_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    course_code  TEXT NOT NULL,
    title        TEXT NOT NULL,
    credits      INTEGER NOT NULL,
    department   TEXT
);

CREATE TABLE faculty (
    faculty_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name   TEXT NOT NULL,
    last_name    TEXT NOT NULL,
    email        TEXT UNIQUE NOT NULL,
    department   TEXT
);

CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id    INTEGER NOT NULL,
    course_id     INTEGER NOT NULL,
    faculty_id    INTEGER,
    semester      TEXT NOT NULL,
    year          INTEGER NOT NULL,
    grade         TEXT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id)  REFERENCES courses(course_id),
    FOREIGN KEY (faculty_id) REFERENCES faculty(faculty_id)
);

INSERT INTO students (first_name, last_name, email, major, level, enrollment_year) VALUES
('Alice', 'Johnson', 'alice.johnson@example.edu', 'Computer Science', 'Undergraduate', 2023),
('Bob', 'Singh', 'bob.singh@example.edu', 'Data Science', 'Graduate', 2024);

INSERT INTO courses (course_code, title, credits, department) VALUES
('CS101', 'Introduction to Programming', 3, 'Computer Science'),
('DS510', 'Data Mining', 3, 'Data Science');

INSERT INTO faculty (first_name, last_name, email, department) VALUES
('Dr. Ajay', 'Kumar', 'ajay.kumar@example.edu', 'Computer Science'),
('Dr. Ye Il', 'Kwon', 'yeil.kwon@example.edu', 'Data Science');

INSERT INTO enrollments (student_id, course_id, faculty_id, semester, year, grade) VALUES
(1, 1, 1, 'Fall', 2024, 'A'),
(2, 2, 2, 'Spring', 2025, 'B+');

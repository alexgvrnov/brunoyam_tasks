import sqlite3
import os.path


def db_create():

    conn = sqlite3.connect('db_task8_1.sqlite')
    cur = conn.cursor()

    q1 = '''CREATE TABLE IF NOT EXISTS Students 
            (id int PRIMARY KEY,
             name varchar(32),
             surname varchar(32),
             age int,
             city varchar(32))'''

    q2 = '''CREATE TABLE IF NOT EXISTS Courses
            (id int PRIMARY KEY,
             name varchar(32),
             time_start date char(8),
             time_finish date char(8))'''

    q3 = '''CREATE TABLE IF NOT EXISTS Students_courses
            (student_id int,
             course_id int,
             FOREIGN KEY (student_id) REFERENCES Students(id),
             FOREIGN KEY (course_id) REFERENCES Courses(id))'''

    cur.execute(q1)
    cur.execute(q2)
    cur.execute(q3)

    students = [(1, 'Max', 'Brooks', 24, 'Spb'), (2, 'John', 'Stones', 15, 'Spb'),
                (3, 'Andy', 'Wings', 45, 'Manchester'), (4, 'Kate', 'Brooks', 34, 'Spb')]
    courses = [(1, 'python', '21.07.21', '21.08.21'), (2, 'java', '13.07.21', '16.08.21')]
    student_courses = [(1, 1), (2, 1), (3, 1), (4, 2)]

    cur.executemany("INSERT INTO Students VALUES (?, ?, ?, ?, ?)", students)
    cur.executemany("INSERT INTO Courses VALUES (?, ?, ?, ?)", courses)
    cur.executemany("INSERT INTO Students_courses VALUES (?, ?)", student_courses)

    conn.commit()
    conn.close()


def db_query():

    conn = sqlite3.connect('db_task8_1.sqlite')
    cur = conn.cursor()

    q1 = '''SELECT name, surname FROM Students Where age > 30'''

    q2 = '''SELECT Students.name, Students.surname FROM Students
             JOIN Students_courses ON Students_courses.student_id = Students.id
             JOIN Courses ON Students_courses.course_id = Courses.id
             WHERE Courses.name = "python"'''

    q3 = '''SELECT Students.name, Students.surname FROM Students
             JOIN Students_courses ON Students_courses.student_id = Students.id
             JOIN Courses ON Students_courses.course_id = Courses.id
             WHERE Courses.name = "python" AND Students.city = "Spb"'''

    cur.execute(q1)
    print(cur.fetchall())

    cur.execute(q2)
    print(cur.fetchall())

    cur.execute(q3)
    print(cur.fetchall())

    conn.close()


if not os.path.exists('db_task8_1.sqlite'):
    db_create()

db_query()

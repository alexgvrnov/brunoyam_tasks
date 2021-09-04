import sqlite3
import os.path


def db_create():

    conn = sqlite3.connect('db_task8_1.sqlite')
    cur = conn.cursor()

    q1 = '''CREATE TABLE IF NOT EXISTS student 
            (id int PRIMARY KEY,
             name varchar(32),
             surname varchar(32),
             age int,
             city varchar(32))'''

    q2 = '''CREATE TABLE IF NOT EXISTS course
            (id int PRIMARY KEY,
             name varchar(32),
             time_start date char(8),
             time_finish date char(8))'''

    q3 = '''CREATE TABLE IF NOT EXISTS student_course
            (student_id int REFERENCES Student(id),
             course_id int REFERENCES Course(id))'''

    cur.execute(q1)
    cur.execute(q2)
    cur.execute(q3)

    students = [(1, 'Max', 'Brooks', 24, 'Spb'), (2, 'John', 'Stones', 15, 'Spb'),
                (3, 'Andy', 'Wings', 45, 'Manchester'), (4, 'Kate', 'Brooks', 34, 'Spb')]
    courses = [(1, 'python', '21.07.21', '21.08.21'), (2, 'java', '13.07.21', '16.08.21')]
    student_courses = [(1, 1), (2, 1), (3, 1), (4, 2)]

    cur.executemany("INSERT INTO student VALUES (?, ?, ?, ?, ?)", students)
    cur.executemany("INSERT INTO course VALUES (?, ?, ?, ?)", courses)
    cur.executemany("INSERT INTO student_course VALUES (?, ?)", student_courses)

    conn.commit()
    conn.close()


def db_query():

    conn = sqlite3.connect('db_task8_1.sqlite')
    cur = conn.cursor()

    q1 = '''SELECT name, surname FROM student Where age > 30'''

    q2 = '''SELECT student.name, student.surname FROM student
             JOIN student_course ON student_course.student_id = student.id
             JOIN course ON student_course.course_id = course.id
             WHERE course.name = "python"'''

    q3 = '''SELECT student.name, student.surname FROM student
             JOIN student_course ON student_course.student_id = student.id
             JOIN course ON student_course.course_id = course.id
             WHERE course.name = "python" AND student.city = "Spb"'''

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

import sqlite3

connection = sqlite3.connect("university.db")
cursor = connection.cursor()

cursor.executescript(
    """
    DROP TABLE IF EXISTS grades;
    DROP TABLE IF EXISTS courses;
    DROP TABLE IF EXISTS students;

    CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    );

    CREATE TABLE courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price INTEGER NOT NULL
    );

    CREATE TABLE grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        grade INTEGER NOT NULL,

        FOREIGN KEY (student_id)
            REFERENCES students (id),

        FOREIGN KEY (course_id)
            REFERENCES courses (id)
    );
    """
)

students = [
    ("Alice", 20),
    ("Bob", 22),
    ("Charlie", 19),
    ("David", 21)
]

cursor.executemany(
    """
    INSERT INTO students (name, age)
    VALUES (?, ?)
    """,
    students
)

courses = [
    ("Python", 15000),
    ("SQL", 10000),
    ("Django", 20000),
    ("Fast API", 25000)
]

cursor.executemany(
    """
    INSERT INTO courses (name, price)
    VALUES (?, ?)
    """,
    courses
)

grades = [
    (1, 1, 90),
    (1, 2, 85),
    (2, 1, 80),
    (2, 3, 95),
    (3, 2, 75),
    (3, 4, 88),
    (4, 1, 92),
    (4, 3, 89)
]

cursor.executemany(
    """
    INSERT INTO grades (student_id, course_id, grade)
    VALUES (?, ?, ?)
    """,
    grades
)

connection.commit()

cursor.execute(
    "SELECT id, name, price FROM courses"
)

for course in cursor.fetchall():
    print(course)

print("\n List of students:")

cursor.execute(
    "SELECT id, name, age FROM students"
)

for student in cursor.fetchall():
    print(student)

print("\n List of grades:")

cursor.execute(
    """
    select 
        students.name,
        courses.name,
        grades.grade
    from grades

    join students on students.id = grades.student_id

    join courses on courses.id = grades.course_id
    """
)

for grade in cursor.fetchall():
    print(grade)


print( "\n BEST GRADE:")

cursor.execute("""
    SELECT
        students.name,
        MAX(grades.grade) AS best_grade

    FROM students

    JOIN grades
        ON students.id = grades.student_id

    GROUP BY students.id, students.name
""")

for row in cursor.fetchall():
    print(row)

print("\n=== WORST GRADE ===")

cursor.execute("""
    SELECT
        students.name,
        MIN(grades.grade) AS worst_grade

    FROM students

    JOIN grades
        ON students.id = grades.student_id

    GROUP BY students.id, students.name
""")

for row in cursor.fetchall():
    print(row)
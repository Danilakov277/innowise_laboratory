"""
Student Grades Manager — database creation script.
This script creates the SQLite database `school.db`,
initializes all required tables, and inserts sample data.

Requirements:
- Python 3.x
- No external libraries needed (uses sqlite3 from the standard library)
"""

import sqlite3

def create_connection(db_name: str) -> sqlite3.Connection:
    """
    Create and return a database connection.
    
    Args:
        db_name (str): Name of the SQLite database file.
    Returns:
        sqlite3.Connection: Active database connection.
    """
    return sqlite3.connect(db_name)


def create_tables(conn: sqlite3.Connection) -> None:
    """
    Create the required tables: students and grades.
    
    Args:
        conn (sqlite3.Connection): Active database connection.
    """
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS grades;")
    cursor.execute("DROP TABLE IF EXISTS students;")

    cursor.execute(
        """
        CREATE TABLE students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            birth_year INTEGER NOT NULL
        );
        """
    )

    cursor.execute(
        """
        CREATE TABLE grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            subject TEXT NOT NULL,
            grade INTEGER NOT NULL CHECK (grade BETWEEN 1 AND 100),
            FOREIGN KEY (student_id) REFERENCES students(id)
        );
        """
    )

    # Optional: create indexes for faster queries
    cursor.execute("CREATE INDEX idx_grades_student ON grades(student_id);")
    cursor.execute("CREATE INDEX idx_grades_subject ON grades(subject);")

    conn.commit()


def insert_data(conn: sqlite3.Connection) -> None:
    """
    Insert sample data into the students and grades tables.
    
    Args:
        conn (sqlite3.Connection): Active database connection.
    """
    cursor = conn.cursor()

    # Insert Students
    students_data = [
        ("Alice Johnson", 2005),
        ("Brian Smith", 2004),
        ("Carla Reyes", 2006),
        ("Daniel Kim", 2005),
        ("Eva Thompson", 2003),
        ("Felix Nguyen", 2007),
        ("Grace Patel", 2005),
        ("Henry Lopez", 2004),
        ("Isabella Martinez", 2006)
    ]

    cursor.executemany(
        "INSERT INTO students (full_name, birth_year) VALUES (?, ?);",
        students_data
    )

    # Insert Grades
    grades_data = [
        (1, "Math", 88), (1, "English", 92), (1, "Science", 85),

        (2, "Math", 75), (2, "History", 83), (2, "English", 79),

        (3, "Science", 95), (3, "Math", 91), (3, "Art", 89),

        (4, "Math", 84), (4, "Science", 88), (4, "Physical Education", 93),

        (5, "English", 90), (5, "History", 85), (5, "Math", 88),

        (6, "Science", 72), (6, "Math", 78), (6, "English", 81),

        (7, "Art", 94), (7, "Science", 87), (7, "Math", 90),

        (8, "History", 77), (8, "Math", 83), (8, "Science", 80),

        (9, "English", 96), (9, "Math", 89), (9, "Art", 92)
    ]

    cursor.executemany(
        "INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?);",
        grades_data
    )

    conn.commit()


def main() -> None:
    """
    Main execution function: creates the database,
    builds tables, and inserts all sample data.
    """
    print("Creating database school.db ...")
    conn = create_connection("school.db")

    print("Creating tables ...")
    create_tables(conn)

    print("Inserting sample data ...")
    insert_data(conn)

    conn.close()
    print("Done! File 'school.db' has been created successfully.")


if __name__ == "__main__":
    main()

-- ============================================================
--  Student Grades Manager — SQL schema and queries
--  This file contains:
--      1. CREATE TABLE statements
--      2. INSERT data for students and grades
--      3. Required SELECT queries for the assignment
-- ============================================================


-- ============================
-- 1. CREATE TABLES
-- ============================

DROP TABLE IF EXISTS grades;
DROP TABLE IF EXISTS students;

CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    birth_year INTEGER NOT NULL
);

CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    grade INTEGER NOT NULL CHECK (grade BETWEEN 1 AND 100),
    FOREIGN KEY (student_id) REFERENCES students(id)
);


-- Optional but recommended for speed
CREATE INDEX idx_grades_student ON grades(student_id);
CREATE INDEX idx_grades_subject ON grades(subject);



-- ============================
-- 2. INSERT SAMPLE DATA
-- ============================

-- Students
INSERT INTO students (full_name, birth_year) VALUES
('Alice Johnson', 2005),
('Brian Smith', 2004),
('Carla Reyes', 2006),
('Daniel Kim', 2005),
('Eva Thompson', 2003),
('Felix Nguyen', 2007),
('Grace Patel', 2005),
('Henry Lopez', 2004),
('Isabella Martinez', 2006);


-- Grades
INSERT INTO grades (student_id, subject, grade) VALUES
(1, 'Math', 88), (1, 'English', 92), (1, 'Science', 85),

(2, 'Math', 75), (2, 'History', 83), (2, 'English', 79),

(3, 'Science', 95), (3, 'Math', 91), (3, 'Art', 89),

(4, 'Math', 84), (4, 'Science', 88), (4, 'Physical Education', 93),

(5, 'English', 90), (5, 'History', 85), (5, 'Math', 88),

(6, 'Science', 72), (6, 'Math', 78), (6, 'English', 81),

(7, 'Art', 94), (7, 'Science', 87), (7, 'Math', 90),

(8, 'History', 77), (8, 'Math', 83), (8, 'Science', 80),

(9, 'English', 96), (9, 'Math', 89), (9, 'Art', 92);


-- ============================
-- 3. SELECT QUERIES
-- ============================

-- (3) Find all grades for Alice Johnson
SELECT s.full_name, g.subject, g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE s.full_name = 'Alice Johnson'
ORDER BY g.subject;


-- (4) Average grade per student
SELECT 
    s.full_name,
    ROUND(AVG(g.grade), 2) AS average_grade,
    COUNT(g.id) AS total_grades
FROM students s
LEFT JOIN grades g ON s.id = g.student_id
GROUP BY s.id
ORDER BY average_grade DESC;


-- (5) Students born after 2004
SELECT id, full_name, birth_year
FROM students
WHERE birth_year > 2004
ORDER BY full_name;


-- (6) Subjects and their average grades
SELECT 
    subject,
    ROUND(AVG(grade), 2) AS average_grade
FROM grades
GROUP BY subject
ORDER BY average_grade DESC;


-- (7) Top 3 students by average grade
SELECT
    s.full_name,
    ROUND(AVG(g.grade), 2) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 3;


-- (8) Students who scored below 80 at least once
SELECT DISTINCT
    s.full_name
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.grade < 80
ORDER BY s.full_name;

Знайти 1 студентa із найбільшим середнім балом з усіх предметів.
SELECT 
    s.id, 
    s.name, 
    ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN students s ON s.id = g.student_id
where g.subject_id = 1
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 1;
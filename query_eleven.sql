
--Додаткове
--1. Середній бал, який певний викладач ставить певному студентові
select
	s2."name",
	t.fullname,
	s."name" as subject_name,
	round(avg(g.grade),2) as avg_grades
from students s2  
join grades g on s2.id = g.student_id
join subjects s on g.subject_id = s.id 
join teachers t on s.id = t.teacher_id 
where s2."name" like ('%З%') and t.fullname ilike ('%Фесенко')
group by 1,2,3









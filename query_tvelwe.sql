
--Додаткове
--2. Оцінки студентів у певній групі з певного предмета на останньому занятті
select
	s2.name student_name,
	g2."name" as group_name,
	t.fullname,
	s."name" as subject_name,
	g.grade as last_grade,
	max(g.grade_date) as last_date
from students s2  
join grades g on s2.id = g.student_id
join subjects s on g.subject_id = s.id 
join teachers t on s.id = t.teacher_id 
join groups g2 on s2.group_id = g2.id 
where g.grade_date = (
	select
		max(grade_date) as last_date
	from grades g
)
group by 1,2,3,4,5


select
	max(grade_date) as last_date
from grades g 










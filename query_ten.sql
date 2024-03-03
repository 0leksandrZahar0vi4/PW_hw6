
--10 Список курсів, які певному студенту читає певний викладач
select
	s2."name",
	t.fullname,
	s."name" as subject_name
from students s2  
join grades g on s2.id = g.student_id
join subjects s on g.subject_id = s.id 
join teachers t on s.id = t.teacher_id 
where s2."name" like ('%З%') and t.fullname ilike ('%Фесенко')
group by 1,2,3









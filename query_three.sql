
--3. Знайти середній бал у групах з певного предмета
select
	s2.name,
	s.group_id,
	round(avg(g.grade),2) as avg_grade 
from grades g  
join students s on g.student_id = s.id
join subjects s2 on g.subject_id = s2.id 
where s2.name = 'ручка' and s.group_id = 1
group by 1,2





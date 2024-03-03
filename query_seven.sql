
--7. Знайти оцінки студентів у окремій групі з певного предмета.
select
	s2.name,
	g.grade,
	s.group_id,
	s.name
from grades g  
join students s on g.student_id = s.id
join subjects s2 on g.subject_id = s2.id 
where s2.name = 'ручка' and s.group_id = 2
group by 1,2,3,4





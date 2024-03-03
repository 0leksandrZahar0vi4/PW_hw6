
--9 Знайти список курсів, які відвідує студент
select
	s.name,
	s2.name 
from students s2  
join grades g2 on s2.id = g2.student_id
join subjects s on g2.subject_id = subject_id
where s2.name = 'Онисим Чумаченко'
group by s.name, s2.name



select
	s.name,
	s2.name 
from students s2  
join grades g2 on s2.id = g2.student_id
join subjects s on g2.subject_id = subject_id
where s2.name ilike('%им%')
group by s.name, s2.name






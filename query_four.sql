select
	s."name",
	round(avg(g.grade), 2) as avg_grade
from subjects s 
join grades g on s.id = g.subject_id 
group by 1;
union
select*
from students s ;


--4. Знайти середній бал на потоці (по всій таблиці оцінок)
select
	round(avg(g.grade), 2) as avg_grade
from grades g; 


--5. Знайти які курси читає певний викладач
select *
from teachers t 
join subjects s on t.teacher_id = s.teacher_id
where t.fullname = 'Мілена Яремчук';

select
	s.name,
	round(avg(g2.grade),2) as avg_grade 
from subjects s2 
join grades g2 on s2.id = g2.subject_id 
join students s on g2.student_id = s.id
group by s.name;
 
select
	s.name,
	round(avg(g2.grade),2) as avg_grade 
from subjects s2 
join grades g2 on s2.id = g2.subject_id 
join students s on g2.student_id = s.id
group by s.name;

select
	s2.name,
	g.grade,
	s.group_id,
	s.name,
	avg(g.grade) 
from grades g  
join students s on g.student_id = s.id
join subjects s2 on g.subject_id = s2.id 
where s2.name = 'ручка' and s.id = 3
group by g.grade, s2.name, s.group_id




--8. Знайти середній бал, який ставить певний викладач зі своїх предметів
select
	t.fullname,
	round(avg(grade),2) as avg_grade 
from teachers t  
join subjects s on t.teacher_id = s.teacher_id
join grades g on s.id = g.subject_id 
where t.fullname like ('%ри%')
group by 1






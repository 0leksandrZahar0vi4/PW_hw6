

--5. Знайти які курси читає певний викладач
select *
from teachers t 
join subjects s on t.teacher_id = s.teacher_id
where t.fullname = 'Мілена Яремчук';

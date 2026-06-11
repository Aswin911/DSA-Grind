# Write your MySQL query statement below
with new_table as (
    select 
        d.name as Department,
        e.name as Employee,
        e.salary as Salary,
        dense_rank() over (partition by d.name order by salary desc) as ranking

    from employee e
    left join department d
    on e.departmentId = d.id

)
select Department,Employee,Salary
from new_table
where ranking <= 3;
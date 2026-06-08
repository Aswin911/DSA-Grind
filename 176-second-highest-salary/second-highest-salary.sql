# Write your MySQL query statement below

#using window function
select(
select distinct salary
from(

select 
salary,
dense_rank() over (order by salary desc) as rnk
from employee
) as Rankedsalaries

where rnk = 2
) as SecondHighestSalary;

#using max()
-- select max(salary) as SecondHighestSalary
-- from employee
-- where salary < (select max(salary) from employee)



#using limit and offset
-- select (
--     select distinct salary
--     from Employee
--     order by salary desc
--     limit 1 offset 1
-- ) as SecondHighestSalary;
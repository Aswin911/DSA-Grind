# Write your MySQL query statement below

#using max()
select max(salary) as SecondHighestSalary
from employee
where salary < (select max(salary) from employee)



#using limit and offset
-- select (
--     select distinct salary
--     from Employee
--     order by salary desc
--     limit 1 offset 1
-- ) as SecondHighestSalary;
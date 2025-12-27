# Write your MySQL query statement below
SELECT e.name AS Employee
From Employee e
Join Employee m
On e.managerId = m.id
where e.salary > m.salary

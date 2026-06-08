CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  set N = N-1;
  RETURN (
      # Write your MySQL query statement below.
    select distinct salary
    from employee
    order by salary desc
    limit 1 offset N
  );
END


-- CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
-- BEGIN
--   RETURN (
--       # Write your MySQL query statement below.
--       select(
--         select distinct salary
--         from(
        
--             select 
--             salary,
--             dense_rank() over (order by salary desc) as rnk
--             from employee
--             ) as Rankedsalaries
        
--         where rnk = N
--         limit 1
--         )

--   );
-- END
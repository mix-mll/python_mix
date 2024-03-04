-- cte_avg_sal.SQL
with cte_avg_sal as (

    select
        department,
        avg(salary) as avg_sal
    from employees
)
select
    employee_id,
    employee_name
from employees 
left join cte_avg_sal using (department)
where salary > avg_sal;


-- 
with cte_tenure_rank as (
    select *,
        rank() over (order by date_of_joining asc) as tenure_rank 
    from employees
)
select
    employee_name
from cte_tenure_rank 
where tenure_rank = 3;

/* Write your PL/SQL query statement below */
-- select name as customers from customers where id not in (select customerid from orders);
select c.name as customers from customers c left join orders o
on c.id=o.customerid
where o.customerid is null;
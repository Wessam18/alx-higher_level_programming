-- Write a script that displays the number of records 
SELECT score, count(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;

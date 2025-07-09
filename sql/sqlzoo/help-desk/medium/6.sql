SELECT company_name, COUNT(1) as cc
FROM Issue a
JOIN Caller b ON a.caller_id = b.caller_id
JOIN Customer c ON b.company_ref = c.company_ref 
GROUP BY company_name
HAVING COUNT(1) > 18

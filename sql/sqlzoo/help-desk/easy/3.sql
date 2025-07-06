SELECT status, COUNT(Call_ref) AS Volume
FROM Issue
GROUP BY status

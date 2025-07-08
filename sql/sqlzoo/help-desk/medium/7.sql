SELECT First_name, Last_name
FROM Caller
WHERE Caller_id NOT IN (SELECT Caller_id FROM Issue)

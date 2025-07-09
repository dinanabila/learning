SELECT DATE_FORMAT(call_date, '%Y-%m-%d %T'), first_name, last_name
FROM Caller
JOIN Issue ON Caller.caller_id = Issue.caller_id
WHERE first_name = 'Samantha' AND last_name = 'Hall' AND DATE_FORMAT(call_date, '%Y-%m-%d') = '2017-08-14'

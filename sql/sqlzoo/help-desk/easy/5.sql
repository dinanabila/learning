SELECT DATE_FORMAT(Shift_date, '%Y-%m-%d') AS Shift_date, Shift_type, first_name, last_name 
FROM Shift, Staff
WHERE Shift.Manager = Staff.Staff_code

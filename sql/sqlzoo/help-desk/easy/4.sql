SELECT COUNT(*) AS mlcc 
FROM Issue 
WHERE Assigned_to IN (SELECT Manager FROM Shift WHERE Issue.Assigned_to = Shift.Manager)

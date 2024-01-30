-- create a view
CREATE VIEW need_meeting AS
SELECT * FROM students
WHERE (score < 80) AND
(FLOOR (DATEDIFF(CURRENT_DATE, last_meeting) > 30) OR (ISNULL(last_meeting) = 1));

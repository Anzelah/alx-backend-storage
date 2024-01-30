-- create a view that lists all students that have a score under 80
-- and no last_meeting or more than 1 month.
CREATE VIEW need_meeting AS
SELECT name FROM students
WHERE (score < 80) AND
(FLOOR (DATEDIFF(CURRENT_DATE, last_meeting) > 30) OR (ISNULL(last_meeting) = 1));

-- create a view
CREATE VIEW need_meeting AS
SELECT * FROM students
WHERE (score < 80) AND
(TIMESTAMPDIFF((MONTH, last_meeting, CURDATE()) > 1 )
OR (ISNULL(last_meeting) = 1));

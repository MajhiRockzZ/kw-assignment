-- All employee data
SELECT *
FROM hr_employee;

-- All college data
SELECT *
FROM kw_college;

-- All stream data
SELECT *
FROM kw_stream;

-- All semester data
SELECT *
FROM kw_semester;

-- All subject data
SELECT *
FROM kw_subject;

-- SELECT name, gender, marital FROM hr_employee WHERE emp_college_id=1;
-- SELECT subject_name FROM kw_subject WHERE subject_semester_id=1;
-- SELECT subject_name, subject_mark FROM kw_subject;

/* ==== [OUTPUT QUERY KW_ASSIGNMENT] ==== */

-- All data.
SELECT *
FROM hr_employee AS EMPLOYEE,
     kw_college AS COLLEGE,
     kw_stream AS STREAM,
     kw_semester AS SEMESTER,
     kw_subject AS SUBJECT
WHERE EMPLOYEE.emp_college_id = COLLEGE.id
  AND COLLEGE.id = STREAM.stream_college_id
  AND STREAM.id = SEMESTER.semester_stream_id
  AND SEMESTER.id = SUBJECT.subject_semester_id;

-- 1. Employee name with subject name with subject Marks.
SELECT EMPLOYEE.name, SUBJECT.subject_name, SUBJECT.subject_mark
FROM hr_employee AS EMPLOYEE,
     kw_college AS COLLEGE,
     kw_stream AS STREAM,
     kw_semester AS SEMESTER,
     kw_subject AS SUBJECT
WHERE EMPLOYEE.emp_college_id = COLLEGE.id
  AND COLLEGE.id = STREAM.stream_college_id
  AND STREAM.id = SEMESTER.semester_stream_id
  AND SEMESTER.id = SUBJECT.subject_semester_id;

-- College name with student count with marks more than 90.
SELECT COUNT(EMPLOYEE.name) AS STUDENTS_WITH_MARKS_MORE_THAN_90
FROM hr_employee AS EMPLOYEE,
     kw_college AS COLLEGE,
     kw_stream AS STREAM,
     kw_semester AS SEMESTER,
     kw_subject AS SUBJECT
WHERE EMPLOYEE.emp_college_id = COLLEGE.id
  AND COLLEGE.id = STREAM.stream_college_id
  AND STREAM.id = SEMESTER.semester_stream_id
  AND SEMESTER.id = SUBJECT.subject_semester_id
  AND SUBJECT.subject_mark >= 90;

-- College wise student count
SELECT COUNT(EMPLOYEE.name) AS STUDENT_WITH_COLLEGE_DRIEMS
FROM hr_employee AS EMPLOYEE,
     kw_college AS COLLEGE
WHERE EMPLOYEE.emp_college_id = COLLEGE.id
  AND COLLEGE.college_name = 'DRIEMS';

-- Subject wise average marks


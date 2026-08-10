CREATE DATABASE student1;
USE student1;
CREATE TABLE stu(
student_id  INT,
student_name  VARCHAR(100),
gender  VARCHAR(10),
age  INT,
city  VARCHAR(50),
course  VARCHAR(100),
fees  DECIMAL(10,2),
joining_date  DATE);

CREATE DATABASE employee;

USE employee;

CREATE TABLE emp(
emp_id  INT,
emp_name VARCHAR(100),
department  VARCHAR(50),
salary  DECIMAL(10,2),
city  VARCHAR(50),
joining_date  DATE )

CREATE DATABASE orders;

USE orders;

CREATE TABLE order1(
order_id INT,
customer_name VARCHAR(100),
product VARCHAR(100),
quantity INT,
price DECIMAL(10,2),
order_date DATE);

USE student1;

INSERT INTO stu VALUES (101, 'Rahul', 'Male', 20, 'Hyd', 'Python', 15000, '2026-01-15');

INSERT INTO stu VALUES (102, 'Priya', 'Female', 19, 'Chennai', 'Java', 18000, '2026-02-10');

INSERT INTO stu VALUES (103, 'Arun', 'Male', 21, 'Bangalore', 'Data Analyst', 25000.00, '2026-03-05');

INSERT INTO stu VALUES (104, 'Sneha', 'Female', 20, 'Delhi', 'Full Stack', 30000.00, '2026-01-25');

INSERT INTO stu VALUES (105, 'Kiran', 'Male', 22, 'Hyd', 'Python', 15000.00, '2026-04-18');


INSERT INTO stu VALUES (105, 'Kiran', 'Male', 22, 'Hyd', 'java',10000, '2026-04-18');

SELECT * FROM stu;

SELECT student_name, city FROM stu;

SELECT * FROM stu WHERE city='hyd';

SELECT * FROM stu WHERE fees>25000;

SELECT * FROM WHERE age BETWEEN 18 AND 25;

SELECT * FROM  stu WHERE student_name LIKE 'A%';

SELECT * FROM stu WHERE student_name LIKE '%K';

SELECT * FROM stu WHERE course IN ('JAVA','PYTHON');

SELECT * FROM stu ORDER BY fees DESC;

SELECT * FROM stu LIMIT 3;

SELECT COUNT(*) FROM stu;

SELECT MAX(fees) FROM stu;

USE employee;

INSERT INTO emp VALUES(1,'hari','development',20000,'vjy','2026-01-15');

INSERT INTO emp VALUES(2,'sai','testing',30000,'rjy','2026-07-12');

INSERT INTO emp VALUES(3,'krishna','api',40000,'hyd','2026-06-03');

INSERT INTO emp VALUES(4,'sri','development',30000,'hyd','2026-03-18');

INSERT INTO emp VALUES(5,'siri','deployment',50000,'chennai','2026-02-22');

SELECT MIN(salary) FROM emp;

SELECT AVG(salary) FROM emp GROUP BY department;

USE student1;

SELECT SUM(fees) FROM stu;

SELECT city,COUNT(*) FROM stu GROUP BY city;

USE employee;

SELECT emp_id,emp_name FROM emp WHERE salary>(SELECT AVG(salary) FROM emp);

USE student1;

SELECT * FROM stu WHERE joining_date > '2024-01-01';

SELECT DISTINCT course FROM stu;

USE employee;

SELECT * FROM emp ORDER BY salary DESC LIMIT 3;

2nd highest salary

SELECT salary FROM emp WHERE salary BETWEEN 30000 AND 60000;

USE orders;
INSERT INTO order1 VALUES (101, 'Rahul', 'Laptop', 2, 50000.00, '2026-01-15');

INSERT INTO order1 VALUES (102, 'Priya', 'Mouse', 10, 500.00, '2026-02-10');

INSERT INTO order1 VALUES (103, 'Arun', 'Keyboard', 6, 1200.00, '2026-03-05');

INSERT INTO order1 VALUES (104, 'Sneha', 'Monitor', 3, 15000.00, '2026-03-12');

INSERT INTO order1 VALUES (105, 'Kiran', 'Laptop', 1, 55000.00, '2026-04-18');

SELECT * FROM order1 WHERE quantity>5;

SELECT order_id,customer_name,(quantity*price) AS total_amt FROM order1;

SELECT product, COUNT(*) FROM order1 GROUP BY product;

SELECT order_id,customer_name,(quantity*price) AS total_amt FROM order1 WHERE (quantity*price)>=50000;

USE employee;

SELECT emp_name FROM emp WHERE emp_name LIKE '%ri%';

USE student1;

SELECT * FROM stu WHERE city='hyd' AND course='python';

USE employee;

SELECT * FROM emp;

SELECT department, salary FROM emp GROUP BY department ORDER BY department,salary;

USE student1;

SELECT city, COUNT(*) AS total_students FROM stu GROUP BY city ORDER BY total_students DESC LIMIT 1;




















































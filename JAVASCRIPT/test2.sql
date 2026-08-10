CREATE DATABASE mysql_joins_exam; 

USE mysql_joins_exam; 

CREATE TABLE departments (
 dept_id INT PRIMARY KEY,
 dept_name VARCHAR(50),
 location VARCHAR(50) ); 
 
 INSERT INTO departments VALUES 
 (1,'HR','Hyderabad'), 
 (2,'IT','Bangalore'),
 (3,'Finance','Chennai'),
 (4,'Marketing','Mumbai'),
 ( 5,'Sales','Delhi'); 
 
 
 CREATE TABLE employees (
  emp_id INT PRIMARY KEY, 
  emp_name VARCHAR(50),
  gender VARCHAR(10), 
  salary DECIMAL(10,2),
  hire_date DATE, 
  dept_id INT ); 
  
  INSERT INTO employees VALUES
   (101,'Rahul','Male',45000,'2023-01-10',1), 
   (102,'Priya','Female',60000,'2022-03-15',2), 
   (103,'Amit','Male',55000,'2021-05-20',2),
   (104,'Sneha','Female',50000,'2020-08-11',3), 
   (105,'Kiran','Male',70000,'2019-09-18',4),
   (106,'Anjali','Female',48000,'2022-11-25',NULL),
   (107,'Ravi','Male',40000,'2024-01-05',2),
   (108,'Pooja','Female',65000,'2021-12-12',5),
   (109,'Arjun','Male',52000,'2023-04-08',NULL),
   (110,'Deepika','Female',58000,'2022-06-14',3); 
   
   CREATE TABLE projects (
    project_id INT PRIMARY KEY, 
    project_name VARCHAR(100),
    start_date DATE,
    emp_id INT ); 
    
    INSERT INTO projects VALUES 
    (201,'Hospital Management System','2024-01-10',101), 
    (202,'E-Commerce Website','2024-02-15',102), 
    (203,'Payroll System','2024-03-20',104), 
    (204,'Inventory Management','2024-04-12',105), 
    (205,'AI Chatbot','2024-05-01',107),
    (206,'Banking Portal','2024-06-10',110),
    (207,'School ERP','2024-07-05',NULL), 
    (208,'CRM Application','2024-08-08',108); 
    
    CREATE TABLE clients (
     client_id INT PRIMARY KEY,
     client_name VARCHAR(100),
     country VARCHAR(50),
     project_id INT ); 
     
     
     INSERT INTO clients VALUES 
     (1,'ABC Technologies','India',201),
     (2,'Global Soft','USA',202),
     (3,'NextGen Solutions','Canada',203),
     (4,'Smart Systems','UK',204),
     (5,'Tech Innovators','Australia',205), 
     (6,'Future Corp','Germany',208),
     (7,'Digital World','India',NULL); 
     SELECT * FROM employees;
     SELECT * FROM departments;
     
     INNER JOIN 
     
     SELECT employees.emp_name, departments.dept_name FROM employees INNER JOIN departments ON employees.dept_id=departments.dept_id;
     SELECT employees.emp_name,employees.emp_name,departments.location FROM employees INNER JOIN departments ON employees.dept_id=departments.dept_id;
     SELECT * FROM employees INNER JOIN departments WHERE dept_name='it';
     SELECT employees.emp_name,departments.dept_name,employees.salary FROM employees INNER JOIN departments ON employees.dept_id=departments.dept_id;
     SELECT * FROM employees INNER JOIN departments ON employees.dept_id=departments.dept_id WHERE employees.gender='female';
     SELECT * FROM employees INNER JOIN departments ON employees.dept_id=departments.dept_id WHERE departments.dept_name='finance';
     SELECT employees.emp_name, departments.dept_name ,employees.salary FROM employees INNER JOIN departments ON employees.dept_id=departments.dept_id WHERE salary>55000;
     SELECT employees.emp_name FROM employees INNER JOIN departments ON employees.dept_id=departments.dept_id WHERE hire_date>  2022-01-01;
     SELECT employees.emp_name, departments.location FROM employees INNER JOIN departments ON employees.dept_id=departments.dept_id ORDER BY employees.emp_name;
     SELECT employees.emp_name, departments.dept_name, departments.location FROM employees INNER JOIN departments ON employees.dept_id=departments.dept_id;
     
     
     LEFT JOIN
     
     SELECT employees.emp_name,departments.dept_name FROM employees LEFT JOIN departments ON employees.dept_id=departments.dept_id;
     SELECT employees.emp_name,departments.dept_name FROM employees LEFT JOIN departments ON employees.dept_id=departments.dept_id WHERE departments.dept_name IS NULL ;
     SELECT employees.emp_name,IFNULL (departments.dept_name,'no department') AS department FROM employees LEFT JOIN departments ON employees.dept_id=departments.dept_id WHERE departments.dept_name IS NULL  ;
     SELECT employees.emp_name, departments.location FROM employees LEFT JOIN departments ON employees.dept_id=departments.dept_id;
     SELECT COUNT(employees.emp_id), departments.dept_name FROM employees LEFT JOIN departments ON employees.dept_id=departments.dept_id GROUP BY departments.dept_id;
     
     
     RIGHT JOIN
     
     select departments.dept_name from employees right join departments on employees.dept_id=departments.dept_id;
     insert into departments values (6,'testing','vizag');
     select departments.dept_name, count(employees.emp_id) as emp_count from employees right join departments on employees.dept_id=departments.dept_id group by departments.dept_name HAVING COUNT(employees.emp_id) = 0;
     select employees.emp_name, departments.dept_name from employees right join departments on employees.dept_id=departments.dept_id;
     select departments.dept_name, employees.salary from employees right join departments on employees.dept_id=departments.dept_id;
     select departments.dept_name, employees.emp_name from employees right join departments on employees.dept_id=departments.dept_id order by departments.dept_name;
     
     
    
     multiple table joins
     
     select employees.emp_name,projects.project_name from employees inner join projects on employees.emp_id=projects.emp_id;
     SELECT employees.emp_name, departments.dept_name,projects.project_name FROM employees INNER JOIN departments ON employees.dept_id=departments.dept_id inner join projects on employees.emp_id=projects.emp_id;
     select projects.project_name, clients.client_name from projects inner join clients on projects.project_id=clients.project_id;
     select employees.emp_name, projects.project_name, clients.client_name from employees inner join projects on employees.emp_id=projects.emp_id inner join clients on projects.project_id=clients.project_id;
     SELECT employees.emp_name, departments.dept_name, projects.project_name, clients.client_name FROM employees INNER JOIN departments ON employees.dept_id=departments.dept_id inner join projects on  employees.emp_id=projects.emp_id inner join clients on projects.project_id=clients.project_id;
     
     
    Interview & Advanced 
    
     SELECT employees.emp_name FROM employees LEFT JOIN projects  ON employees.emp_id=projects.emp_id WHERE projects.emp_id IS NULL ;
     SELECT projects.project_name FROM projects LEFT JOIN employees ON employees.emp_id=projects.emp_id WHERE employees.emp_id IS NULL;
     SELECT clients.client_name FROM clients LEFT JOIN projects ON clients.project_id=projects.project_id WHERE projects.project_id IS NULL;
     SELECT COUNT(employees.emp_id) AS emp_count , departments.dept_name FROM employees INNER JOIN departments ON employees.dept_id=departments.dept_id GROUP BY departments.dept_id, departments.dept_name ORDER BY emp_count DESC;
     SELECT employees.emp_id,employees.emp_name,departments.dept_name,projects.project_name,clients.client_name,employees.salary,departments.location FROM employees INNER JOIN departments ON employees.dept_id=departments.dept_id INNER JOIN projects ON employees.emp_id=projects.emp_id INNER JOIN clients ON projects.project_id=clients.project_id;
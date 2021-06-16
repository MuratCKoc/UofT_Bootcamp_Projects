--Data Analysis
--List the following details of each employee: employee number, last name, first name, sex, and salary.

select employees.emp_no AS "Employee_no",
	employees.last_name AS "Last_name",
	employees.first_name AS "First_name",
	employees.sex AS "Sex",
	salaries.salary AS "Wage"
from employees
join salaries on employees.emp_no = salaries.emp_no

--List first name, last name, and hire date for employees who were hired in 1986.
select employees.first_name AS "First_name",
	employees.last_name AS "Last_name",
	employees.hire_date AS "Date"
from employees where employees.hire_date >= '1986-01-01'

--List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.

select employees.last_name AS "Last_name",
	employees.first_name AS "First_name",
	employees.emp_no AS "Employee_number",
	departments.dept_name AS "Department_name",
	dept_manager.dept_no AS "Department_number"
from employees
inner join dept_manager on dept_manager.emp_no = employees.emp_no
inner join departments on dept_manager.dept_no = departments.dept_no
order by "Department_number" ASC;

--List the department of each employee with the following information: employee number, last name, first name, and department name.

select departments.dept_name AS "Department Name",
	employees.emp_no AS "Employee Number",
	employees.last_name AS "Last Name",
	employees.first_name AS "First Name"
from departments
inner join dept_employees on departments.dept_no = dept_employees.dept_no
inner join employees on dept_employees.emp_no = employees.emp_no
order by "Department Name" DESC;

--List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."

select employees.emp_no AS "Employee_no",
	employees.first_name AS "First_name",
	employees.last_name AS "Last_name",
	employees.sex AS "Sex"
from employees
where (employees.first_name = 'Hercules' AND employees.last_name LIKE 'B%');

--List all employees in the Sales department, including their employee number, last name, first name, and department name.

select departments.dept_name AS "Department Name",
	employees.emp_no AS "Employee Number",
	employees.last_name AS "Last Name",
	employees.first_name AS "First Name"
from departments
inner join dept_employees on departments.dept_no = dept_employees.dept_no
inner join employees on dept_employees.emp_no = employees.emp_no
where departments.dept_name = 'Sales';

--List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.

select departments.dept_name AS "Department Name",
	employees.emp_no AS "Employee Number",
	employees.last_name AS "Last Name",
	employees.first_name AS "First Name"
from departments
inner join dept_employees on departments.dept_no = dept_employees.dept_no
inner join employees on dept_employees.emp_no = employees.emp_no
where departments.dept_name = 'Sales' OR departments.dept_name = 'Development';

--In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.

select count(last_name) AS total,last_name
from employees
group by last_name
order by total DESC;


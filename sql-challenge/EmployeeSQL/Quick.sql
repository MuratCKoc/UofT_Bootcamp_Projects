CREATE TABLE Departments(
	dept_no VARCHAR(10) NOT NULL,
	dept_name VARCHAR(50),
	PRIMARY KEY (dept_no)
);

CREATE TABLE Titles(
	title_id VARCHAR (10) PRIMARY KEY, 
	title VARCHAR(50)
);

CREATE TABLE Employees(
	emp_no INT PRIMARY KEY NOT NULL, 
	emp_title_id VARCHAR(10),
	birth_date DATE,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	sex VARCHAR(3),
	hire_date DATE, 
	FOREIGN KEY (emp_title_id) REFERENCES Titles(title_id)
);
 
CREATE TABLE Dept_Employees(
	emp_no INT,
	dept_no VARCHAR(10),
	PRIMARY KEY(emp_no, dept_no),
	FOREIGN KEY (emp_no) REFERENCES Employees(emp_no),
	FOREIGN KEY (dept_no) REFERENCES Departments(dept_no)
);

CREATE TABLE Dept_Manager(
	dept_no VARCHAR(10),
	emp_no INT PRIMARY KEY NOT NULL, 
	FOREIGN KEY (emp_no) REFERENCES Employees(emp_no),
	FOREIGN KEY (dept_no) REFERENCES Departments(dept_no)
);

CREATE TABLE Salaries(
	emp_no INT PRIMARY KEY,
	salary INT, 
	FOREIGN KEY (emp_no) REFERENCES Employees(emp_no)
);

--import order = dept, titles, employees, dept_emp, dept_man, salaries
-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employee_id serial PRIMARY KEY,
	first_name varchar(20) NOT NULL,
	last_name varchar(20) NOT NULL,
	title varchar(100),
	birth_date date NOT NULL,
	notes text
);
SELECT * FROM employees;

CREATE TABLE customers
(
	customer_id varchar(5) PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name varchar(100) NOT NULL
);

SELECT * FROM customers;

CREATE TABLE orders
(
	order_id serial PRIMARY KEY,
	customer_id varchar(5) REFERENCES customers(customer_id) NOT NULL,
	employee_id int REFERENCES employees(employee_id) NOT NULL,
	order_date date Not NULL,
	ship_sity varchar(30)
);

SELECT * FROM customers;
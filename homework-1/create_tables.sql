-- SQL-команды для создания таблиц
CREATE TABLE employees
(
    employee_id int PRIMARY KEY,
	first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    title varchar(50) NOT NULL,
    birth_date date,
	notes text
);

CREATE TABLE customers
(
    customer_id varchar(10) PRIMARY KEY,
    company_name varchar(100) NOT NULL,
    contact_name varchar(100) NOT NULL
);

CREATE TABLE orders
(
	order_id int,
    customer_id varchar(10) NOT NULL UNIQUE REFERENCES customers(customer_id),
    employee_id int UNIQUE REFERENCES employees(employee_id),
    order_date date,
	ship_city varchar(100) NOT NULL
);



# compare2mysqldbtable
Python script to compare 2 MySQL Databases and compare rows for a specific table

Python:

Install packages for Python:

> pip install pandas

> pip install sqlalchemy

> pip install mysql-connector-python

Database:

Install MySQL 8.0.31 (or preferred as per your requirement)

> Create 2 Databases

> payroll_dev, payroll_qa

> Create 1 table in both the Databases

> employee and run below sql queries

DROP TABLE IF EXISTS `employee`;

CREATE TABLE IF NOT EXISTS `employee` (

  `employee_id` int NOT NULL AUTO_INCREMENT,
  
  `employee_name` varchar(50) NOT NULL,
  
  `employee_age` smallint NOT NULL,
  
  `employee_sex` char(1) NOT NULL,
  
  PRIMARY KEY (`employee_id`)
  
) ENGINE=MyISAM AUTO_INCREMENT=1234568 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Employee Details';

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`employee_id`, `employee_name`, `employee_age`, `employee_sex`) VALUES

(1234567, 'Test1', 38, 'M'),

(234567, 'Test2', 39, 'M'),

(234568, 'Test3', 40, 'M'),

(234569, 'Test4', 41, 'F');

COMMIT;

> Create 2nd table in both the Databases
> payroll and run below sql queries

DROP TABLE IF EXISTS payroll;

CREATE TABLE IF NOT EXISTS payroll (
    payroll_id INT,
    employee_id INT,
    date DATE NOT NULL,
    PRIMARY KEY (payroll_id),
    FOREIGN KEY (employee_id) REFERENCES employee (employee_id)
    
--
-- Dumping data for table `payroll`
--

INSERT INTO payroll (payroll_id, employee_id, date) VALUES (123456, 1234567, '2023-01-01'); 

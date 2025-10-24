
# MySQL - Basic SQL Concepts

## Description
This project covers fundamental concepts and SQL commands used to manage databases, users, and relationships in **MySQL 8.0**.  
It focuses on creating users, assigning privileges, understanding keys and constraints, and performing complex queries using subqueries, JOINs, and UNIONs.

---

## General Objectives

### 1. How to create a new MySQL user
To create a new user in MySQL:
```sql
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
````

This command creates a user named **username** with the specified **password**, who can connect from **localhost**.

---

### 2. How to manage privileges for a user to a database or table

Privileges allow or restrict user access to certain databases or tables.

Grant privileges:

```sql
GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'localhost';
```

Remove privileges:

```sql
REVOKE ALL PRIVILEGES ON database_name.* FROM 'username'@'localhost';
```

Apply changes:

```sql
FLUSH PRIVILEGES;
```

---

### 3. What’s a PRIMARY KEY

A **PRIMARY KEY** uniquely identifies each record in a table.

* It must contain **unique** values.
* It **cannot** be **NULL**.

Example:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
```

---

### 4. What’s a FOREIGN KEY

A **FOREIGN KEY** enforces a relationship between two tables.
It links a column in one table to a **PRIMARY KEY** in another.

Example:

```sql
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

---

### 5. How to use NOT NULL and UNIQUE constraints

* **NOT NULL** ensures that a column cannot have a NULL value.
* **UNIQUE** ensures that all values in a column are different.

Example:

```sql
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL
);
```

---

### 6. How to retrieve data from multiple tables in one request

You can retrieve data from several tables using **JOIN** operations.

Example:

```sql
SELECT users.name, orders.id
FROM users
JOIN orders ON users.id = orders.user_id;
```

---

### 7. What are subqueries

A **subquery** is a query inside another query, used to perform operations based on the result of another SQL statement.

Example:

```sql
SELECT name
FROM users
WHERE id IN (SELECT user_id FROM orders WHERE total > 100);
```

---

### 8. What are JOIN and UNION

* **JOIN** combines rows from two or more tables based on a related column.

  ```sql
  SELECT *
  FROM users
  INNER JOIN orders ON users.id = orders.user_id;
  ```

* **UNION** combines results of two or more **SELECT** statements.

  ```sql
  SELECT name FROM users
  UNION
  SELECT name FROM employees;
  ```

---

## Requirements

* **Allowed editors:** `vi`, `vim`, `emacs`
* **Environment:** Ubuntu 20.04 LTS, MySQL 8.0 (version 8.0.25)
* All files must:

  * End with a new line
  * Start with a comment describing the task
  * Include a comment before each SQL query
  * Use **uppercase** for all SQL keywords (`SELECT`, `WHERE`, etc.)
* A `README.md` file is mandatory at the root of the project
* The length of your files will be tested using `wc`

---
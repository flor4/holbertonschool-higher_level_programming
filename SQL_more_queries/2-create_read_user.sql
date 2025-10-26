-- Create the database (won’t fail if it already exists)
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user (won’t fail if it already exists)
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege only on this database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Reload privilege tables
FLUSH PRIVILEGES;

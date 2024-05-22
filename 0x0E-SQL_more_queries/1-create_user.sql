-- 0d. Create a user with the name user_0d_1 and password user_0d_1_pwd. Grant all privileges to the user on all databases. Flush privileges.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;

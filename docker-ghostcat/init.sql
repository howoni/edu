CREATE USER 'edu'@'%' IDENTIFIED BY 'edu230515!@';
GRANT SELECT ON mydb.* TO 'edu'@'%';
CREATE DATABASE mydb;
USE mydb;
CREATE TABLE users (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL
);
INSERT INTO users (name, email) VALUES
  ('Alice', 'alice@example.com'),
  ('Bob', 'bob@example.com'),
  ('Flag', 'Flag{hello meow}');


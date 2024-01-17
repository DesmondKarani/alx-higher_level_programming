-- Script to create database hbtn_0d_2 and user user_0d_2 with specific privileges

-- Creating the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Creating the user if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Granting SELECT privilege to the user on the hbtn_0d_2 database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;

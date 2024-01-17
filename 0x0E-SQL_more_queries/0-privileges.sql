-- Script to list privileges for user_0d_1 and user_0d_2

-- Checking privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Separator for clarity
SELECT '-----';

-- Checking privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';

-- Script to list all cities of California from the hbtn_0d_usa database

SELECT id, name 
FROM cities 
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;

-- lists all records of the table second_table of the database hbtn_0c_0
SELECT score, TRIM(name) AS name
FROM second_table
WHERE name IS NOT NULL AND TRIM(name) != ''
ORDER BY score DESC;
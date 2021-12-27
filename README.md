# SQL_Notes
Repository to keep all my learning materials and note of SQL. 

***

### SQL Keywords & Examples

Keywords | Examples | Description
--- | --- | --- | --- 
SELECT | SELECT * FROM tbl | Select all rows and column from the table 'tbl' |  
SELECT | SELECT c1,c2 FROM tbl | Select all rows and column c1,c2 from the table 'tbl' | 
SELECT | SELECT c1,c2 FROM tbl WHERE Conditions ORDER BY c1 ASC, c2 DESC| Select all rows and column c1,c2 from the table 'tbl' where conditions order the result by c1 in ascending order and c2 in descending order |   
SELECT | SELECT DISTINCT c1,c2 FROM tbl | Select distinct all rows and column c1,c2 from the table 'tbl' | 
SELECT | SELECT c1, aggregate(expr) FROM tbl GROUP BY c1| Select column c1 and use aggregate function on expression expr, group columns by column c1 | 
SELECT | SELECT c1, aggregate(expr) AS c2 FROM tbl GROUP BY c1 HAVING c2 > v| Select column c1 and cs as column alias of the result of aggregate function on expr. Filter group of records with c2 greater than value v |
INSERT INTO | INSERT INTO tbl (c1, c2, ...) VALUES (v1, v2, ...) | Insert data into table 'tbl' |
INSERT INTO | INSERT INTO tbl (c1, c2, ...) SELECT c1, c2.. FROM tb2 WHERE conditions | Insert data from 'tbl2' into table 'tbl' |
UPDATE | UPDATE tbl SET c1 = v1, c2 = v2 ... WHERE conditions | Update data in table 'tbl'|
DELETE | DELETE FROM tbl WHERE conditions | Delete records from table based on WHERE conditions |
TRUNCATE | TRUNCATE TABLE tbl | Drop table 'tbl' and re-create it, all data is lost |
INNER JOIN | SELECT * FROM tb1 INNER JOIN tb2 ON join-conditions | Inner join table 'tb1' with 'tb2' based on join-conditions |
LEFT JOIN | SELECT * FROM tb1 LEFT JOIN tb2 ON join-conditions | Left join table 'tb1' with 'tb2' based on join-conditions |
RIGHT JOIN | SELECT * FROM tb1 RIGHT JOIN tb2 ON join-conditions | Right join table 'tb1' with 'tb2' based on join-conditions |
CREATE TABLE | CREATE TABLE tbl (c1 datatype(length) PRIMARY KEY) | Create table 'tbl' with primary key is c1 |
DROP TABLE | DROP TABLE tbl | Remove table 'tbl' from database |
ALTER TABLE | ALTER TABLE tbl ADD COLUMN c1 datatype (length) | Add column c1 to table 'tbl' |
ALTER TABLE | ALTER TABLE tbl DROP COLUMN c1 | Drop column c1 to table 'tbl' |


# SQL_Notes
Repository to keep all my learning materials and note of SQL. 

***

### Setup
- Download and install PostgreSQL : https://www.postgresql.org/download/
- Download and install pgadmin4 : https://www.pgadmin.org/download/pgadmin-4-windows/

***

### SQL Keywords & Examples

Keywords | Examples | Description
--- | --- | --- 
SELECT | SELECT * FROM tbl | Select all rows and column from the table 'tbl' 
SELECT | SELECT c1,c2 FROM tbl | Select all rows and column c1,c2 from the table 'tbl' 
SELECT | SELECT c1,c2 FROM tbl WHERE Conditions ORDER BY c1 ASC, c2 DESC| Select all rows and column c1,c2 from the table 'tbl' where conditions order the result by c1 in ascending order and c2 in descending order 
SELECT | SELECT DISTINCT c1,c2 FROM tbl | Select distinct all rows and column c1,c2 from the table 'tbl' 
SELECT | SELECT c1, aggregate(expr) FROM tbl GROUP BY c1| Select column c1 and use aggregate function on expression expr, group columns by column c1 |
SELECT | SELECT c1, aggregate(expr) AS c2 FROM tbl GROUP BY c1 HAVING c2 > v| Select column c1 and cs as column alias of the result of aggregate function on expr. Filter group of records with c2 greater than value v 
INSERT INTO | INSERT INTO tbl (c1, c2, ...) VALUES (v1, v2, ...) | Insert data into table 'tbl' 
INSERT INTO | INSERT INTO tbl (c1, c2, ...) SELECT c1, c2.. FROM tb2 WHERE conditions | Insert data from 'tbl2' into table 'tbl' 
UPDATE | UPDATE tbl SET c1 = v1, c2 = v2 ... WHERE conditions | Update data in table 'tbl'
DELETE | DELETE FROM tbl WHERE conditions | Delete records from table based on WHERE conditions 
TRUNCATE | TRUNCATE TABLE tbl | Drop table 'tbl' and re-create it, all data is lost 
INNER JOIN | SELECT * FROM tb1 INNER JOIN tb2 ON join-conditions | Inner join table 'tb1' with 'tb2' based on join-conditions 
LEFT JOIN | SELECT * FROM tb1 LEFT JOIN tb2 ON join-conditions | Left join table 'tb1' with 'tb2' based on join-conditions 
RIGHT JOIN | SELECT * FROM tb1 RIGHT JOIN tb2 ON join-conditions | Right join table 'tb1' with 'tb2' based on join-conditions 
CREATE TABLE | CREATE TABLE tbl (c1 datatype(length) PRIMARY KEY) | Create table 'tbl' with primary key is c1 
DROP TABLE | DROP TABLE tbl | Remove table 'tbl' from database 
ALTER TABLE | ALTER TABLE tbl ADD COLUMN c1 datatype (length) | Add column c1 to table 'tbl' 
ALTER TABLE | ALTER TABLE tbl DROP COLUMN c1 | Drop column c1 to table 'tbl' 

***

### SQL Notes
**PostgreSQL vs. MySQL: Which Is Better?**
If you’re developing an application with a database back end, which of the two should you use? Consider **PostgreSQL for any application that might grow to enterprise scope, with complex queries and frequent write operations.** If you’re new to the world of databases and don’t expect your application to scale up, or you’re looking for a **quick tool for prototyping, then consider MySQL.**

References: https://www.fivetran.com/blog/postgresql-vs-mysql


**SQL and RDBMS**
RDBMS is kind of database SW to keep the data organized into a particular kind of table. Example of RDBMS are PostgreSQL, MySQL, Sqlite. 
SQL is a language used to access and control RDBMS. Almost all the RDBMS accept instructions in SQL, although the SQL they accept differs in small details.


**NoSQL vs RDBMS**
- scalability
NoSQL scale well whereas RDBMS does not.
- Join table
RDBMS can join multiple tables easily whereas NoSQL cannot.
- Data analysis
RDBMS - Data analysis and querying can be done easily. 
NoSQL - More to real time data analysis.

RDBMS focus more on relationship and NoSQL focus more on storage.
You can consider using NoSQL when your RDBMS reaches bottlenecks. NoSQL makes RDBMS more flexible.

Not all data is relational. For those situations, NoSQL can be helpful.

With that said, NoSQL stands for "Not Only SQL". It's not intended to knock SQL or supplant it.

SQL has several very big advantages:

Strong mathematical basis.
- Declarative syntax.
- A well-known language in Structured Query Language (SQL).

Those haven't gone away.

References: https://stackoverflow.com/questions/4160732/nosql-vs-relational-database

**When should use NoSQL over RDBMS?**

**Handling A Large Number Of Read Write Operations**

Look towards NoSQL databases when you need to scale fast. And when do you generally need to scale fast?

When there are a large number of read-write operations on your website & when dealing with a large amount of data, NoSQL databases fit best in these scenarios. Since they have the ability to add nodes on the fly, they can handle more concurrent traffic & big amount of data with minimal latency.

**Flexibility With Data Modeling**

The second cue is during the initial phases of development when you are not sure about the data model, the database design, things are expected to change at a rapid pace. NoSQL databases offer us more flexibility.

**Eventual Consistency Over Strong Consistency**

It’s preferable to pick NoSQL databases when it’s OK for us to give up on Strong consistency and when we do not require transactions.

A good example of this is a social networking website like Twitter. When a tweet of a celebrity blows up and everyone is liking and re-tweeting it from around the world. Does it matter if the count of likes goes up or down a bit for a short while?

The celebrity would definitely not care if instead of the actual 5 million 500 likes, the system shows the like count as 5 million 250 for a short while.

When a large application is deployed on hundreds of servers spread across the globe, the geographically distributed nodes take some time to reach a global consensus.

Until they reach a consensus, the value of the entity is inconsistent. The value of the entity eventually gets consistent after a short while. This is what Eventual Consistency is.

Though the inconsistency does not mean that there is any sort of data loss. It just means that the data takes a short while to travel across the globe via the internet cables under the ocean to reach a global consensus and become consistent.

We experience this behaviour all the time. Especially on YouTube. Often you would see a video with 10 views and 15 likes. How is this even possible?

It’s not. The actual views are already more than the likes. It’s just the count of views is inconsistent and takes a short while to get updated.

**Running Data Analytics**

NoSQL databases also fit best for data analytics use cases, where we have to deal with an influx of massive amounts of data.

References: https://stackoverflow.com/questions/3713313/when-should-i-use-a-nosql-database-instead-of-a-relational-database-is-it-okay


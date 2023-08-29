#                                                                 ques - 1

"""A database is an organized collection of data, so that it can be easily accessed and managed.The main purpose of the database
is to operate a large amount of information by storing, retrieving, and managing data.

SQL : SQL databases are primarily called Relational Databases (RDBMS).These databases have fixed or static or predefined schema
      These databases are not suited for hierarchical data storage.These databases are best suited for complex queries.
      Examples: MySQL, PostgreSQL, Oracle, MS-SQL Server, etc 
      
NOSQL : NoSQL databases are primarily called non-relational or distributed databases.They have a dynamic schema
        These databases are best suited for hierarchical data storage.These databases are not so good for complex queries.
        Examples: MongoDB, GraphQL, HBase, Neo4j, Cassandra, etc

 """     

 #                                                               ques - 2

"""DDL : Data Definition Language (DDL) is used to create and modify the structure of objects in a database using predefined
         commands and a specific syntax.DDL consist of Commands to commands like CREATE, ALTER, TRUNCATE and DROP.
         
CREATE : This command is used to create a new table in SQL. it takes table name,column name and datatype 
example : CREATE TABLE Student_info
(
College_Id number(10),
College_name varchar(30),
Branch varchar(10)
);

ALTER : This command is used to add, delete or change columns in the existing table.The user needs to know the existing table
        name and can do add, delete or modify tasks easily. 
        
exapmle : ALTER TABLE Student_info
ADD CGPA number;

DROP : This command is used to remove an existing table along with its structure from the Database.
example : DROP TABLE Student_info;

TRUNCATE : This command is used to remove all rows from the table, but the structure of the table still exists.
example : TRUNCATE TABLE table_name; 

"""
#                                                                 ques - 3
"""DML : (Data manipulation language) it it respnosible to manipulation in data.It is the component of the SQL statement that
         controls access to data and to the database. 
         
INSERT :  It is used to insert data into a table.
example : INSERT INTO Student VALUES 
('5','HARSH','WEST BENGAL',
'XXXXXXXXXX','19');

UPDATE : It is used to update existing data within a table.
example : UPDATE table_name SET column1 = value1, column2 = value2,
            WHERE condition;
            
DELETE : It is used to delete records from a database table. 
example : DELETE FROM table_name WHERE some_condition;
DELETE FROM GFG_EMPLOyees WHERE NAME = 'Rithvik';

"""
#                                                                ques - 4
""" DQL : (Data query language) DQL statements are used for performing queries on the data within schema objects. The purpose of 
          the DQL Command is to get some schema relation based on the query passed to it.  
          
SELECT : It is used to retrieve data from the database.
example : SELECT * FROM table_name; 
SELECT CustomerName, LastName FROM Customer;

"""

#                                                                ques - 5
""" PRIMARY KEY : A primary key generally focuses on the uniqueness of the table. It is a column or a set of columns that uniquely
                  distinguishes every row in the database. It means it should not have any duplicate value. Also, it doesn't 
                  contain a NULL value.

    FOREIGN KEY : A foreign key is generally used to build a relationship between the two tables. The major purpose of the foreign
                  key is to sustain data integrity between two separate instances of an entity.

"""

#                                                                ques - 6
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
mydb.close()

""" cursor() : A cursor is an object which helps to execute the query and fetch the records from the database

    execute() : This method executes the given database operation (query or command). 
    
"""

#                                                              ques - 7
""" order of execution of clause in sql query 
    1.   FROM : Tables are joined to get the base data. 
    2.   WHERE : The base data is filtered.
    3.   GROUP BY : The filtered base data is grouped.
    4.   HAVING : The grouped base data is filtered.
    5.   SELECT : The final data is returned.
    6.   ORDER BY : The final data is sorted.
    7.   LIMIT : The returned data is limited to row count

""" 
# Some useful SQL queries for Teradata 

### Tables in a database in Teradata
SELECT DISTINCT TableName FROM DBC.Columns WHERE DatabaseName='PROD_EDW_SAS_ADHOC_VIEWS';

### Column names of a table in Teradata
SELECT DISTINCT ColumnName FROM DBC.Columns WHERE DatabaseName='PROD_EDW_SAS_ADHOC_VIEWS' AND TableName='VW_SHOPPING_TRANSACTION';

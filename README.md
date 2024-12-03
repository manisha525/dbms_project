# dbms_project

**About the Project :**
This project demonstrates the implementation of database transactions in PostgreSQL while ensuring compliance with the ACID properties (Atomicity, Consistency, Isolation, and Durability). It uses Python with the psycopg2 library to perform transactions that manage product and depot information in a database.
The project is part of an assignment to showcase the handling of SQL transactions with real-world constraints like referential integrity, error handling, and cascading updates.

**Features**
1. Transaction 4: The depot d1 changes its name to dd1 in Depot and Stock.

2. Transaction 5: We add a product (p100, cd, 5) in Product and (p100, d2, 50) in Stock.

3. ACID Property Demonstration:
- Atomicity: Ensures all operations within a transaction are executed or none at all.
- Consistency: Maintains database integrity by adhering to constraints and rules.
- Isolation: Uses the SERIALIZABLE isolation level to ensure no interference from concurrent transactions.
- Durability: Ensures changes persist once the transaction commits.

4. Error Handling:
- Rollbacks changes in case of errors like primary key violations or constraint breaches.
- Ensures the database remains consistent even when exceptions occur.

**Technologies Used**
- Database: PostgreSQL
- Programming Language: Python
- Python Libraries:
  - psycopg2: For interacting with PostgreSQL.
  - tabulate: For displaying table data in a structured format.

**How to Run**
Clone this repository and navigate to the project directory.
Run the command in your Python Terminal:
python transaction.py

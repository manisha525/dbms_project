import psycopg2
from tabulate import tabulate
print("psycopg2 and tabulate are installed and working.")

print("Beginning")

# Connect to the database
con = psycopg2.connect(
    host="localhost",
    database="postgres",  # Replace with your database name
    user="postgres",  # Replace with your PostgreSQL username
    password="password"
)

print("Connected to the database.")

# Set transaction properties
con.set_isolation_level(3)  # SERIALIZABLE isolation level
con.autocommit = False  # For atomicity

try:
    cur = con.cursor()

    # Display the initial state of the tables
    print("\nBefore Transactions:")
    print("Product Table:")
    cur.execute("SELECT * FROM Product;")
    results = cur.fetchall()
    print(tabulate(results, headers=["prod_id", "pname", "price"], tablefmt="grid"))

    print("\nDepot Table:")
    cur.execute("SELECT * FROM Depot;")
    results = cur.fetchall()
    print(tabulate(results, headers=["dep_id", "addr", "volume"], tablefmt="grid"))

    print("\nStock Table:")
    cur.execute("SELECT * FROM Stock;")
    results = cur.fetchall()
    print(tabulate(results, headers=["prod_id", "dep_id", "quantity"], tablefmt="grid"))

    # Transaction 4: Rename depot 'd1' to 'dd1'
    print("\nExecuting Transaction 4: Rename depot 'd1' to 'dd1'")
    cur.execute("UPDATE Depot SET dep_id = 'dd1' WHERE dep_id = 'd1';")
    cur.execute("UPDATE Stock SET dep_id = 'dd1' WHERE dep_id = 'd1';")
    print("Transaction 4 completed successfully.")

    # Transaction 5: Add product 'p100' and its stock
    print("\nExecuting Transaction 5: Add product 'p100' and its stock")
    cur.execute("INSERT INTO Product (prod_id, pname, price) VALUES ('p100', 'cd', 5);")
    cur.execute("INSERT INTO Stock (prod_id, dep_id, quantity) VALUES ('p100', 'd2', 50);")
    print("Transaction 5 completed successfully.")

    # Commit the transaction
    con.commit()
    print("\nTransactions committed successfully.")

    # Display the final state of the tables
    print("\nAfter Transactions:")
    print("Product Table:")
    cur.execute("SELECT * FROM Product;")
    results = cur.fetchall()
    print(tabulate(results, headers=["prod_id", "pname", "price"], tablefmt="grid"))

    print("\nDepot Table:")
    cur.execute("SELECT * FROM Depot;")
    results = cur.fetchall()
    print(tabulate(results, headers=["dep_id", "addr", "volume"], tablefmt="grid"))

    print("\nStock Table:")
    cur.execute("SELECT * FROM Stock;")
    results = cur.fetchall()
    print(tabulate(results, headers=["prod_id", "dep_id", "quantity"], tablefmt="grid"))

except (Exception, psycopg2.DatabaseError) as err:
    print(f"Error: {err}")
    print("Transactions could not be completed, so database will be rolled back.")
    con.rollback() # Rolls back all changes made in the transaction if any error occurs

finally:
    if con:
        cur.close()
        con.close()
        print("PostgreSQL connection is now closed.")

print("End")

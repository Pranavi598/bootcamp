import sqlite3
import random
import time

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create the COMPANIES table if it doesn't exist
cursor.execute('''
               CREATE TABLE IF NOT EXISTS COMPANIES
               (
                   company_name
                   TEXT,
                   id
                   INTEGER
               )
               ''')


# Function to generate 500 insert statements
def generate_inserts(num_inserts):
    companies = ["Agatha", "Xentrix", "Apple", "Google", "Microsoft", "IBM", "Tesla", "Amazon", "Facebook", "Intel"]
    inserts = []

    for i in range(num_inserts):
        company = random.choice(companies)
        company_id = i + 1
        inserts.append(f'INSERT INTO COMPANIES (company_name, id) VALUES ("{company}", {company_id});')

    return inserts


# Start timing the insertions
start_time = time.time()

# Generate the insert statements
insert_statements = generate_inserts(500)

# Execute each insert statement
for statement in insert_statements:
    cursor.execute(statement)

# Commit the changes and close the connection
conn.commit()

# End timing the insertions
end_time = time.time()

# Print the time taken to execute the inserts
print(f"Time taken for 500 inserts: {end_time - start_time:.4f} seconds")

# Close the connection
conn.close()
import sqlite3
import ollama

# ==========================================
# TEXT-TO-SQL WORKFLOW USING OLLAMA
# ==========================================

print("=" * 55)
print("TEXT-TO-SQL WORKFLOW USING OLLAMA")
print("=" * 55)

# Connect to SQLite database
connection = sqlite3.connect("college.db")
cursor = connection.cursor()

# Get question from user
question = input("\nEnter your question: ")

# ==========================================
# STEP 1: Generate SQL using Ollama
# ==========================================

print("\nGenerating SQL query...\n")

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"""
You are a Text-to-SQL assistant.

Convert the user's question into a valid SQLite SQL query.

Database table:
students

Columns:
id INTEGER
name TEXT
department TEXT
cgpa REAL

User question:
{question}

Rules:
1. Return ONLY the SQL query.
2. Do not use markdown.
3. Do not explain the query.
"""
        }
    ]
)

# Get generated SQL
sql_query = response["message"]["content"].strip()

# Remove markdown if Ollama accidentally adds it
sql_query = sql_query.replace("```sql", "")
sql_query = sql_query.replace("```", "")
sql_query = sql_query.strip()

print("Generated SQL:")
print(sql_query)

# ==========================================
# STEP 2: Execute SQL Query
# ==========================================

print("\nExecuting query...\n")

try:
    cursor.execute(sql_query)
    results = cursor.fetchall()

    # Check whether results exist
    if results:
        print("Results:")
        print("-" * 55)

        for row in results:
            print(row)

        print("-" * 55)
    else:
        print("No records found.")

except sqlite3.Error as error:
    print("SQL Error:", error)

# Close database connection
connection.close()

print("\nProgram completed successfully!")

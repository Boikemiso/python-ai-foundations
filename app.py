import json
import requests
import sqlite3

# --- PART 1: Reading the local JSON file ---
print("Reading local JSON file")

with open("data.json", "r") as file:
    data = json.load(file)

print(f"Company: {data["company"]}")
print(f"Role: {data["role"]}")

print("Skills Required:")
for skill in data["skills_required"]:
    print(f"{skill}")

# --- PART 2: Calling the API (HTTP/JSON) ---
print("\nFetching from API")

try:
    response = requests.get("https://official-joke-api.appspot.com/random_joke")

    joke_data = response.json()

    print(joke_data["setup"])
    print(joke_data["punchline"])

except Exception as e:
    print("Error: Could not connect to the API.")
    print(f"Details: {e}")

# --- PART 3: Basic SQL ---
print("Saving to database")

# Connect to a database
conn = sqlite3.connect("jokes.db")
cursor = conn.cursor()

# Created table
cursor.execute("""
   CREATE TABLE IF NOT EXISTS saved_jokes(
      id INTEGER PRIMARY KEY,
      setup TEXT,
      punchline TEXT
)
""")

if "joke_data" in locals():
    cursor.execute(
        "INSERT INTO saved_jokes(setup, punchline) VALUES(?, ?)",
        (joke_data["setup"], joke_data["punchline"]),
    )
    conn.commit()
    print("Joke successfully saved to database!")

    cursor.execute("SELECT * FROM saved_jokes")
    print(f"Database now contains {len(cursor.fetchall())} joke(s).")

conn.close()

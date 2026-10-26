import json
import requests

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

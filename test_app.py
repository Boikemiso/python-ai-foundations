import json


def test_json_reading():
    with open("data.json", "r") as file:
        data = json.load(file)

    # The assert checks if the is exactly what we expect
    assert data["company"] == "Bluespec Holdings"
    assert "Python" in data["skills_required"]

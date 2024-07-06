import os
import json

def create_test_files():
    sandbox_input_dir = os.path.join("sandbox", "input")
    os.makedirs(sandbox_input_dir, exist_ok=True)

    # Create test_text.txt
    with open(os.path.join(sandbox_input_dir, "test_text.txt"), "w") as f:
        f.write("""This is a sample text file for testing the File Encryption Utility.
It contains multiple lines of plain text.
Feel free to encrypt and decrypt this file to test the functionality.""")

    # Create test_json.json
    json_data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York",
        "interests": ["programming", "cryptography", "data science"],
        "is_student": False
    }
    with open(os.path.join(sandbox_input_dir, "test_json.json"), "w") as f:
        json.dump(json_data, f, indent=2)

    # Create test_csv.csv
    csv_content = """Name,Age,City,Occupation
Alice,25,London,Engineer
Bob,32,Paris,Designer
Charlie,28,Berlin,Teacher
Diana,35,Rome,Doctor"""
    with open(os.path.join(sandbox_input_dir, "test_csv.csv"), "w") as f:
        f.write(csv_content)

    print("Test files created successfully in the sandbox/input directory.")

if __name__ == "__main__":
    create_test_files()
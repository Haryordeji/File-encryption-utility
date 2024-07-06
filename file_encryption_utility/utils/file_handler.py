import os
import random

def secure_delete_file(file_path: str, passes: int = 3):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    file_size = os.path.getsize(file_path)

    for _ in range(passes):
        with open(file_path, 'wb') as f:
            f.write(os.urandom(file_size))

    os.remove(file_path)

def create_sandbox_directories():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    input_dir = os.path.join(base_dir, "sandbox", "input")
    output_dir = os.path.join(base_dir, "sandbox", "output")

    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
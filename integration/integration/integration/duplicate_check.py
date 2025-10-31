import os
import csv

def is_duplicate(file_path, log_path="upload_logs.csv"):
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    
    with open(log_path, "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            existing_name = row[0]
            if existing_name == file_name:
                print(f"Duplicate detected: {file_name}")
                return True
    return False

# Example usage
print(is_duplicate("test_order1.pdf"))

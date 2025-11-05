import os
from duplicate_check import is_duplicate

def test_duplicate_detection():
    # Make a temporary log file for testing
    log = "test_upload_logs.csv"
    with open(log, "w") as f:
        f.write("file_name,upload_time,user_id,S3_URL,Upload_Status\n")
        f.write("test_order1.pdf,2025-10-30T10:00:00Z,alyssa,s3://bucket/test_order1.pdf,Success\n")

    # Run tests
    assert is_duplicate("test_order1.pdf", log) == True
    assert is_duplicate("new_order.pdf", log) == False
    os.remove(log)
    print("✅ Duplicate detection tests passed!")

if __name__ == "__main__":
    test_duplicate_detection()

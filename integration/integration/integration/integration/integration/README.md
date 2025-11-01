# Data Pipeline / Integration - Alyssa Cintron

## Overview
Implements structured upload tracking and integration flow for the NOMOS Auto Intake system.  
This part of the project focuses on recording uploads, detecting duplicates, defining the JSON schema, and visualizing the data flow.

---

## 1. Upload Logging
Extended `upload_logs.csv` to include:
- `S3_URL`
- `Upload_Status` ("Success" / "Failed")

**Example:**
test_order1.pdf,2025-10-30T10:00:00Z,alyssa,s3://varsity-order-intake-test/test_order1.pdf,Success

---

### 2. Duplicate Detection
Checks existing uploads by filename before accepting new files.

```python
def is_duplicate(file_path, log_path="upload_logs.csv"):
{
  "file_name": "test_order1.pdf",
  "order_number": "ORD-12345",
  "styles": [{ "style_number": "ST-987", "color": "Red", "quantity": 120 }],
  "comments": "Rush order"
}
User Upload → S3 Storage → OCR Extraction → Review Interface

    ...

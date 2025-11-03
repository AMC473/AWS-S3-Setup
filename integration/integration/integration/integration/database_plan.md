# Database Migration Plan (CSV → SQLite)

## Purpose
Move from flat CSV logging to a structured SQLite database for better data management and scalability.

## Proposed Table: uploads
| Column | Type | Description |
|---------|------|-------------|
| id | INTEGER PRIMARY KEY | Unique identifier |
| file_name | TEXT | Name of uploaded file |
| upload_time | TEXT | Timestamp of upload |
| user_id | TEXT | Uploader name or ID |
| s3_url | TEXT | Cloud storage location |
| upload_status | TEXT | "Success" / "Failed" |
| extraction_status | TEXT | "Pending" / "Success" / "Failed" |

## Migration Steps
1. Read data from `upload_logs.csv`
2. Create the `uploads` table in SQLite
3. Insert all CSV records into the table
4. Verify record count and data integrity
5. Deprecate CSV once database fully tested

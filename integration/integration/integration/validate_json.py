import json
from jsonschema import validate, ValidationError

# Load your defined schema
with open("extracted_text_schema.json") as f:
    schema = json.load(f)

# Load a sample OCR output file to test
with open("sample_ocr_output.json") as f:
    data = json.load(f)

try:
    validate(instance=data, schema=schema)
    print("✅ JSON validation successful — matches schema!")
except ValidationError as e:
    print("❌ JSON validation failed:")
    print(e.message)

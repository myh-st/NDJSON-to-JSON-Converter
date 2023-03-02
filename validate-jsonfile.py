import json
import sys

# Check if the input file path is provided
if len(sys.argv) < 2:
    print("Please provide the path to the JSON file as an argument")
    sys.exit()

input_file = sys.argv[1]

# Read the contents of the input file
try:
    with open(input_file) as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"Error: {input_file} not found")
    sys.exit()
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON in {input_file} on line {e.lineno}, column {e.colno}")
    sys.exit()

print(f"{input_file} is a valid JSON file")
print("Contents:")
print(data)

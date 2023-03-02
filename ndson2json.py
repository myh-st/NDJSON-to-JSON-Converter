import subprocess
import argparse
import os
import sys
import ndjson
import json

# Get input file path from command line argument
if len(sys.argv) < 2:
    print("Please provide input file path as command line argument")
    sys.exit(1)

input_file = sys.argv[1]

# Check if input file exists
if not os.path.isfile(input_file):
    print(f"Input file {input_file} not found")
    sys.exit(1)

# Extract the input file name and directory
input_dirname, input_basename = os.path.split(input_file)

# Create output directory if it does not exist
output_dir = os.path.join(input_dirname, "output-json")
os.makedirs(output_dir, exist_ok=True)

# Construct output file name
output_file = os.path.join(output_dir, os.path.splitext(input_basename)[0] + ".json")

def install_ndjson():
    subprocess.check_call(['pip', 'install', 'ndjson'])


try:
    import ndjson
except ModuleNotFoundError:
    print("ndjson is not installed. Installing...")
    install_ndjson()

with open(input_file) as f:
    data = ndjson.load(f)

with open(output_file, 'w') as f:
    json.dump(data, f)

print(f"Output saved to {output_file}")

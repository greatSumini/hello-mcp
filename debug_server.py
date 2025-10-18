"""Debug script to test server responses"""

import subprocess
import json
import time

# Start server
process = subprocess.Popen(
    ["python", "main.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1
)

time.sleep(2)

# Send a request
request = {
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
        "name": "take_a_break",
        "arguments": {}
    },
    "id": 1
}

request_json = json.dumps(request) + "\n"
print(f"Sending request: {request_json}")

process.stdin.write(request_json)
process.stdin.flush()

# Read response
print("Waiting for response...")
response_line = process.stdout.readline()
print(f"Response: {response_line}")

if response_line:
    try:
        response = json.loads(response_line)
        print(f"Parsed response: {json.dumps(response, indent=2)}")
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")

# Read stderr for any errors
time.sleep(1)
process.terminate()

stderr = process.stderr.read()
if stderr:
    print(f"\nStderr output:\n{stderr}")

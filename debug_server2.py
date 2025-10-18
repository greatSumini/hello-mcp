"""Debug script with proper MCP initialization"""

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

# Step 1: Initialize
init_request = {
    "jsonrpc": "2.0",
    "method": "initialize",
    "params": {
        "protocolVersion": "2024-11-05",
        "capabilities": {},
        "clientInfo": {
            "name": "test-client",
            "version": "1.0.0"
        }
    },
    "id": 1
}

print("1. Sending initialize request...")
process.stdin.write(json.dumps(init_request) + "\n")
process.stdin.flush()

init_response = process.stdout.readline()
print(f"Initialize response: {init_response}")

# Step 2: Send initialized notification
initialized_notif = {
    "jsonrpc": "2.0",
    "method": "notifications/initialized"
}

print("\n2. Sending initialized notification...")
process.stdin.write(json.dumps(initialized_notif) + "\n")
process.stdin.flush()

time.sleep(1)

# Step 3: List tools
list_tools_request = {
    "jsonrpc": "2.0",
    "method": "tools/list",
    "id": 2
}

print("\n3. Sending tools/list request...")
process.stdin.write(json.dumps(list_tools_request) + "\n")
process.stdin.flush()

tools_response = process.stdout.readline()
print(f"Tools response: {tools_response}")

if tools_response:
    try:
        tools = json.loads(tools_response)
        print(f"Available tools: {json.dumps(tools, indent=2)}")
    except:
        pass

# Step 4: Call a tool
tool_request = {
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
        "name": "take_a_break",
        "arguments": {}
    },
    "id": 3
}

print("\n4. Sending tool call request...")
process.stdin.write(json.dumps(tool_request) + "\n")
process.stdin.flush()

tool_response = process.stdout.readline()
print(f"Tool response: {tool_response}")

if tool_response:
    try:
        response = json.loads(tool_response)
        print(f"\nParsed tool response: {json.dumps(response, indent=2)}")
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")

# Cleanup
time.sleep(1)
process.terminate()

stderr = process.stderr.read()
if stderr:
    print(f"\nStderr output:\n{stderr}")

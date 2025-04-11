# Claude MCP Client

A Python client for interacting with the Claude API and MCP server.

## Description

This project provides a client interface for the Claude API, allowing you to send messages and receive responses. It also includes functionality to handle tool calls and interact with an MCP server.

## Features

- Send messages to Claude API
- Handle conversation history
- Process tool calls
- Connect to MCP server

## Installation

1. Clone this repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - `CLAUDE_API_KEY`: Your Claude API key
   - `MCP_SERVER_URL`: URL of the MCP server (default: http://localhost:5001)

## Usage

```python
from claude_mcp_client import ClaudeClient

client = ClaudeClient(api_key="your_api_key")
response = client.send_message("Hello, Claude!")
print(response)
```

## License

[MIT License](LICENSE) 
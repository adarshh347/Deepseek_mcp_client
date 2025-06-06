import sys
import os
import requests
import argparse
import json
from claude_mcp_client import ClaudeMCPClient

def check_mcp_server():
    mcp_url = os.environ.get("MCP_SERVER_URL","http://localhost:5001")
    try:
        response = requests.get(f"{mcp_url}/health",timeout=2)
        if response.status_code == 200:
            return True
        return False
    except requests.RequestException:
        return False
    except requests.exceptions.RequestException:
        return False

def main():
    parser = argparse.ArgumentParser(description="Ask Claude MCP")
    parser.add_argument("query",nargs="*",help="question to ask")
    args = parser.parse_args()

    if not os.envrion.get("CLAUDE_API_KEY"):
        print("error in getting CLAUDE_API_KEY")
        sys.exit(1)
    if args.query:
        query = " ".join(args.query)
    else:
        query = input("Ask Claude")
    client = ClaudeMCPClient()
    print(f"Searching for{query}")

    try:
        answer =  client.get_final_answer(query)
        print("Answer: ",answer)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()

    
    

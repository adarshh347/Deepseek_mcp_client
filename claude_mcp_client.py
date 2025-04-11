import os
import json
import requests
import time
from typing import Dict,Any,Optional

CLAUDE_API_KEY = os.environ.get("CLAUDE_API_KEY","")
CLAUDE_API_URL = "https://api.deepseek.com/chat/completions"
MCP_SERVER_URL = os.environ.get("MCP_SERVER_URL","http://localhost:5001")

class ClaudeClient:
    def __init__(self, api_key = CLAUDE_API_KEY, model: str="deepseek-chat"):
        self.api_key = api_key
        self.model = model
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        self.tools =[{
            "name":"fetch_web_content",
            "description": "Retrieves info from website based on user queries",
            "parameters" : {
                "type" : "object",
                "properties" : {
                    "query": {
                        "type":"string",
                        "description" : "the search query or website to look up information about"
                    }
                },
                "required" : ["query"]
            }
        }]

        self._check_mcp_server()
        def send_message(self,message:str, conversation_history: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
            if not self.api_key:
                raise ValueError("api key for deepseek needed")
            
            if conversation_history is None:
                conversation_history = []

            payload = {
                "model" : self.model,
                "max_tokens":4096,
                "messages": conversation_history + [{"role":"user", "content": message}],
                "tools": self.tools,
                "tool_choice":"auto",
                "temperature":0.7
            }
            print("Sending request to deepseek")
            try:
                response=requests.post(
                    CLAUDE_API_KEY,
                    headers=self.headers,
                    json=payload
                )
                if response.status_code !=200:
                    print(response.json())

                    print("Error")
                response.raise_for_status()
                result=response.json()
                print(f"Deepseek response: {result}")

                has_tool_call = False
                tool_call = {}

                choices = result.get("choices",[])
                if choices:
                    message_block=choices[0].get("message",{})
                    tool_calls = message_block.get("tool_calls",[])

                    if tool_calls:
                        has_tool_call=True
                        print("Tool call detected")

                        first_call = tool_calls[0]
                        tool_call["name"] = first_call.get("function",{}).get("name","")
                        tool_call["parameters"] = json.loads(first_call.get("function",{}).get("name",""))
                        
                        print(f"Tool call details:{tool_call}")
                        tool_response = self._handle_tool_call(tool_call)
                        print(f"Tool response: {tool_response}")

                        conversation_history.append({"role": "user", "content": message})
                        conversation_history.append({
                            "role":
                        })


            


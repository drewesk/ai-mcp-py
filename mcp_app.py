import os
from langchain_mcp_adapters.client import MultiServerMCPClient

BRD_API_KEY = os.eviron.get("BRD_API_KEY")

mcp = MultiServerMCPClient()

{
  "mcpServers": {
    "Bright Data": {
      "command": "npx",
      "args": ["@brightdata/mcp"],
      "env": {
        "API_TOKEN": "<insert-your-api-token-here>",
        "RATE_LIMIT": "<optional if you want to change rate limit format: limit/time+unit, e.g., 100/1h, 50/30m, 10/5s>",
        "WEB_UNLOCKER_ZONE": "<optional if you want to override the web unlocker zone name - default is mcp_unlocker>",
        "BROWSER_ZONE": "<optional if you want to override the browser zone name - defaults is mcp_browser>"
      }
    }
  }
}
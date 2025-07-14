import os
from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio

BRD_API_KEY = os.environ.get("BRD_API_KEY")

mcp = MultiServerMCPClient(
{
    "Bright Data": {
      "command": "npx",
      "args": ["@brightdata/mcp"],
      "transport": "stdio",
      "env": {
        "API_TOKEN": BRD_API_KEY,
        "WEB_UNLOCKER_ZONE": "unlocker_mcp_py",
      }
    }
  }
)

async def mcp_tools():
    tools = await mcp.get_tools()

    for idx, tool in enumerate(tools):
        print(idx, tool.name)
        print(tool.args)
        print("********************")

    return tools
async def handle_prompt(tools):
    scraper = tools[1]
    result = await scraper.ainvoke({
        "url": "https://medium.com/ayuth/install-anaconda-on-macos-with-homebrew-c94437d63a37"
    })

    print(result)
    return result

tools = asyncio.run(mcp_tools())
asyncio.run(handle_prompt(tools))
import os
import sys
import asyncio
import itertools
import contextlib
from langchain_ollama import OllamaLLM
from langchain_mcp_adapters.client import MultiServerMCPClient


BRD_API_KEY = os.environ.get("BRD_API_KEY")

if not BRD_API_KEY:
    raise EnvironmentError("BRD_API_KEY is not set in environment variables.")

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

async def run_spinner(message="Thinking...", delay=0.1):
    for frame in itertools.cycle("|/-\\"):
        print(f"\r{message} {frame}", end="", flush=True)
        try:
            await asyncio.sleep(delay)
        except asyncio.CancelledError:
            print("\rDone!            ")
            break

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

    user_prompt = "What is this website?"

    full_prompt = (
        "Context (scraped data):\n\n"
        + result.strip()
        + "\n\nQuestion\n\n"
        + user_prompt
    )

    llm = OllamaLLM(model="WhiteRabbitNeo/WhiteRabbitNeo-2.5-Qwen-2.5-Coder-7B")

    spinner_task = asyncio.create_task(run_spinner("Thinking..."))
    
    try:
        llm_response = await llm.ainvoke(full_prompt)
    finally:
        spinner_task.cancel()
        with contextlib.suppress(asyncio.CancelledError):
            await spinner_task  # Let it exit cleanly

    print(llm_response)
    return llm_response

tools = asyncio.run(mcp_tools())
asyncio.run(handle_prompt(tools))
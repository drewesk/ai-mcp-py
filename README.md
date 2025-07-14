
# 🤖 ai_mcp_py — Local AI-Powered Web Search Assistant

**ai_mcp_py** is a fully local AI assistant that uses Ollama to run a powerful LLM (WhiteRabbitNeo-2.5-Qwen-2.5-Coder-7B) and scrape the web using Bright Data's Unlocker MCP tools — all orchestrated in Python and Streamlit with some Node.js under the hood. No cloud LLMs. No data sharing. Just local compute magic.

> 🔒 Local, Private, and Powerful — because your prompts are nobody else's business.

---

## 🧠 Built With

- Python + Asyncio
- [LangChain](https://www.langchain.com/)
- [Streamlit](https://streamlit.io/)
- [Bright Data MCP](https://brightdata.com/)
- [Ollama](https://ollama.com/)
- Terminal spinner magic courtesy of `itertools`

---

## 🧰 Setup

### 1. 📬 Get Bright Data API Key

- Go to [brightdata.com](https://brightdata.com)
- Under **Proxies and Scraping**, create an `Unlocker_MCP` zone
- Make sure to:
  - Allow *Admin Access*
  - Set token to *never expire*
- Paste the token into your terminal session:

```bash
export BRD_API_KEY=your_token_here
```

> 💸 They offer free credits on signup (no credit card needed). Ignore the payment screens, click through.

---

### 2. 🖥️ Clone the Repo

```bash
git clone https://github.com/drewesk/ai-mcp-py.git
cd ai-mcp-py
```

---

### 3. 🐍 Create Conda Environment (Mac/Linux)

```bash
conda create -n mcp_env python=3.12
conda activate mcp_env
conda install -c conda-forge nodejs
```

> 🧪 Make sure `node`, `npx`, and `conda` work from your terminal. You may need to update your `.zshrc` or `.bashrc`.

---

### 4. 📦 Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. ⚡ Start Bright Data MCP Server

```bash
npx @brightdata/mcp API_TOKEN=$BRD_API_KEY
```

---

### 6. 🧠 Start Ollama + Download Model

In a separate terminal:

```bash
ollama serve
ollama run WhiteRabbitNeo/WhiteRabbitNeo-2.5-Qwen-2.5-Coder-7B // or run you fav model and update mcp_app.py
```

Make sure the model runs **smoothly** on your machine (GPU preferred).

---

## 🧪 Run the App

```bash
streamlit run mcp_app.py
```

Once running, you’ll get a friendly UI to:

- Paste any URL
- Ask any question about that page
- Watch your local AI scrape and synthesize 🤯

---

## 🧼 Example Usage

1. **Paste URL** → `https://medium.com/ayuth/install-anaconda-on-macos-with-homebrew-c94437d63a37`
2. **Prompt** → `"What does this article tell me to do?"`
3. Hit **Submit**, wait for the 🌀 spinner to complete
4. **Voilà!** — you'll see a local LLM-generated summary right on screen

---



## ☁️ Future Ideas

- Add support for multiple LLMs
- Cache scraped content
- Auto-detect article structure
- Run this from the command line without Streamlit

---

## 🐾 Follow / Contribute

Open PRs, make suggestions, or fork for your own personal assistant. The world (wide web) is yours.

---

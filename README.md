# langchain-ollama-projects

My personal learning repo for LangChain + Ollama — building toward agentic AI and LLM-powered automation workflows.

I come from an RPA and full-stack background (Blue Prism, NestJS, Vue), so I learn best by mapping new concepts to things I already understand. 
This repo is where I do that — one working example at a time, running fully local on my machine using Ollama.

---

## Why this repo exists

I've spent 25 years automating business processes. Most of that was rule-based — if this, then that, run the bot. What drew me to LangChain is the shift toward *reasoning-based* automation: give the model context, memory, and tools, then let it figure out the steps. That's a different kind of thinking and I wanted to build intuition for it from the ground up.

Everything here runs locally. No OpenAI API key, no cloud costs, no data leaving my machine. Just Ollama serving a local model and Python doing the work.

---

---

## Projects

### NagaBot — CLI Chatbot with Memory (`/project-cli-chatbot`)

A command-line chatbot that actually remembers what you said earlier in the conversation. Sounds simple, but getting memory working correctly with a local Ollama model taught me more about how LLMs handle context than any tutorial did.

**What it does:**
- Runs a conversational loop in the terminal
- Maintains conversation history across turns using LangChain's message history
- Uses a locally served model via Ollama — no internet required
- Graceful exit on `quit` or `exit`

**The key thing I learned:** LLMs are stateless by default. Every call is a blank slate. "Memory" is just us passing the previous messages back in on every request. Once that clicked, everything else made sense.

---

### Exercises (`/exercises`)

Structured exercises I worked through to understand LangChain fundamentals before building the chatbot. Each file is a standalone runnable script — no setup beyond the requirements below.

Topics covered so far:
- Basic model invocation with `OllamaLLM` and `ChatOllama`
- Prompt templates with `PromptTemplate` and `ChatPromptTemplate`
- Chaining with `|` (LCEL — LangChain Expression Language)
- Output parsers — getting clean strings out of model responses
- Conversation memory patterns

---

## The import pattern that tripped me up

Early on I kept hitting import errors because of how LangChain split its packages. After some trial and error on Windows, here's what actually works:

```python
# Use these — stable and actively maintained
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_ollama import ChatOllama, OllamaLLM

# Avoid this where possible — being phased out for many integrations
# from langchain_community.llms import Ollama  ← use OllamaLLM instead
```

On Windows specifically, if `langchain_ollama` gives you connection issues, this fallback works:

```python
from langchain_community.llms import Ollama
llm = Ollama(model="llama3.2", base_url="http://127.0.0.1:11434")
```

The mental model that helped me:
```
model → message → invoke → response
```
That's the atomic unit of every LangChain application. Everything else — chains, agents, memory, tools — is just building on top of that.

---

## Setup

**Requirements:**
- Python 3.10+
- [Ollama](https://ollama.com/) installed and running locally
- A model pulled — I use `llama3.2` for most exercises

```bash
# Pull the model first
ollama pull llama3.2

# Clone the repo
git clone https://github.com/tristanSilva/langchain-ollama-projects.git
cd langchain-ollama-projects

# Install dependencies
pip install langchain langchain-core langchain-ollama langchain-community
```

**Run the chatbot:**
```bash
cd project-cli-chatbot
python nagatbot.py
```

**Run any exercise:**
```bash
cd exercises
python 01_basic_invoke.py
```

---

## My setup

- OS: Windows 11
- CPU: AMD Ryzen 5
- RAM: 16GB
- Model: llama3.2 via Ollama (runs fine on CPU — no GPU needed for learning)

I specifically wanted a setup that works on a mid-range machine without a dedicated GPU, since that's the reality for a lot of developers in the Philippines. Everything in this repo is optimized for that constraint.

---

## What's next

- Adding tool use / function calling examples
- RAG pipeline — connecting the chatbot to a local document store
- Multi-agent patterns with LangGraph
- Eventually: integrating LLM reasoning into an RPA workflow (LangChain + Power Automate or n8n)

---

## Background

I'm a Business Process Automation Developer at Nestlé Business Services AOA with 25+ years across RPA (Blue Prism, Automation Anywhere), full-stack development (NestJS, Vue.js, React Native), and enterprise solutions. This repo is part of a deliberate push into AI-powered automation — building the skills to design systems where LLMs handle the reasoning and code handles the execution.

If you're coming from an RPA background and trying to figure out where LangChain fits, I hope this repo saves you some of the head-scratching I went through.

---

*Naga City, Philippines*

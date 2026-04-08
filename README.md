# myth-ai-agent
AI agent that generates myth‑style stories with short‑term and long‑term memory.
# Myth AI Agent

A Python‑based AI agent that generates myth‑style stories with **short‑term and long‑term memory**.  
You can extend it with more tools, agents, or LangChain / Agents SDK integration.

---

## Features

- Myth‑style story generation (culture, theme, length).
- Agents layer: `BaseAgent`, `MythAgent`, and LangChain‑based agent.
- Memory layer:
  - Short‑term per‑session memory.
  - Long‑term structured memory with tags and TTL.
  - Vector‑backed semantic search (Chroma).
- Tools:
  - `myth_generator` (direct LLM call).
  - `langchain_tool` (LangChain‑compatible myth generator).

---

## Quick Start

1. Clone:

   ```bash
   git clone https://github.com/johnstonnil-star/myth-ai-agent.git
   cd myth-ai-agent

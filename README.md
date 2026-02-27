# agent-101


# 🚀 AI Business Planning & Execution Agent

An intelligent **AI-powered Business Planning Agent** designed to transform a simple business idea into a  **complete executable business strategy** .

This system autonomously analyzes business goals, plans execution steps, generates marketing strategies, creates email campaigns, and produces actionable task breakdowns — all through a streaming AI workflow.

---

## 🧠 Project Overview

The **AI Business Agent** acts as a virtual business consultant capable of:

* Understanding business objectives
* Performing structured planning
* Executing specialized AI chains
* Reviewing outputs for quality
* Delivering a complete business execution roadmap

The agent follows a **Planner → Executor → Reviewer → Validator** architecture similar to modern autonomous AI systems.

---

## ✨ Key Features

### ✅ Business Strategy Generation

Produces a detailed business overview including:

* Executive summary
* Target audience identification
* Unique Value Proposition (UVP)
* Core customer pain points
* Strategic positioning

---

### 📈 Marketing Strategy Planning

Automatically generates:

* Marketing objectives
* Core messaging strategy
* Recommended marketing channels
* Channel prioritization
* Non-recommended channels with reasoning

---

### 📧 AI Email Campaign Generator

Creates structured marketing email sequences:

* Campaign objectives
* Subject lines
* Email body content
* Conversion-focused Call-To-Actions
* Multi-email campaign flow

---

### 🗂 Task Execution Breakdown

Transforms strategy into executable actions:

* Ordered implementation steps
* Priority classification
* Business impact reasoning
* Operational task descriptions

---

### 📚 Retrieval-Augmented Generation (RAG)

Supports contextual intelligence by allowing users to upload:

* PDF documents
* TXT business notes
* Research files

The agent retrieves relevant knowledge from a vector database to enhance decision quality.

---

### ⚡ Real-Time Streaming AI Execution

Users can observe the agent's reasoning process live:

* Planning phase logs
* Execution stages
* Review improvements
* Validation steps

Powered using **Server-Sent Events (SSE)** for real-time feedback.

---

## 🏗 Architecture

```
User Input
   ↓
Execution Planner
   ↓
RAG Context Retrieval
   ↓
Specialized AI Chains
   ├── Business Chain
   ├── Marketing Chain
   ├── Email Chain
   └── Task Chain
   ↓
Reviewer Agent
   ↓
Schema Validation
   ↓
Final Business Plan Output
```

---

## 🛠 Tech Stack

### Backend

* FastAPI
* Python AsyncIO
* LangChain
* Chroma Vector Database
* StreamingResponse (SSE)

### AI Architecture

* Multi-Agent Execution System
* Planner–Executor Pattern
* Retrieval Augmented Generation (RAG)
* Structured Output Validation

### Frontend

* Vanilla JavaScript
* TailwindCSS
* Real-time Streaming UI

---

## 🔒 Middleware & System Features

* Rate Limiting Middleware
* File Upload Context Processing
* Streaming-safe API responses
* Modular Chain Architecture
* Async Execution Pipeline

---

## 🚀 Running Locally

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/ai-business-agent.git
cd ai-business-agent
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

```bash
export OPENAI_API_KEY="your_api_key"
```

### 5. Run Server

```bash
python main.py
```

Open in browser:

```
http://localhost:8000/app
```

---

## 📦 Example Use Case

Input:

> "Launch a premium mobile car wash service in Toronto"

Output:

* Business Strategy
* Marketing Plan
* Email Campaign
* Execution Roadmap
* Actionable Tasks

---

## ☁ Deployment

Designed for deployment using:

* AWS EC2 / Lightsail
* Render
* Railway
* Docker-based environments

Supports reverse proxy and streaming configurations.

---

## 🎯 Portfolio Value

This project demonstrates:

* Autonomous AI Agent Design
* Production-ready FastAPI Architecture
* Streaming AI Applications
* RAG Implementation
* Middleware Engineering
* Full-stack AI Deployment

---

## 📸 Demo

*(Add screenshots or demo video here)*

---

## 📄 License

MIT License

---

## 👨‍💻 Author

**Tewodros Abisso**

AI & Software Developer
Focused on Intelligent Systems, Backend Engineering, and Autonomous AI Agents.

---

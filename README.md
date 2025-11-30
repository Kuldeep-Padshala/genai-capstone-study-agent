# Smart AI Study Assistant — Multi-Agent LLM System  
*A Generative AI Capstone Project (Agents for Good — Education)*

This project implements a fully offline, multi-agent study assistant that simulates an intelligent AI tutor.  
It demonstrates the key agent features required for the GenAI Capstone:

- **LLM-powered agent** (mocked for offline use)
- **Parallel agents** (content search + flashcard generator)
- **Sequential agents** (quiz generation, guidance)
- **Session & memory** (`InMemorySessionService`)
- **Observability** (logging)
- **Long-running agent simulation** (pause & resume)

---

## 🚀 Features

### 🔹 1. LLM Agent (Mocked)
Generates:
- explanations  
- quizzes  
- summaries  
- prerequisites, key concepts, practice problems  

### 🔹 2. Parallel Agents
Using `ThreadPoolExecutor`:
- `ContentSearchAgent`
- `FlashcardAgent`

### 🔹 3. Sequential Agents
The `StudyCoordinator` orchestrates:
- parallel work  
- then sequential quiz generation  
- then informative Q/A  

### 🔹 4. Memory System
`InMemorySessionService` stores:
- user metadata  
- study plan  
- topics  
- weekly hours  

### 🔹 5. Logging / Observability
All agents log:
- start/finish  
- progress  
- warnings  
- pause/resume  

### 🔹 6. Long-running Operation Agent
Simulates:
- step-wise computation  
- pausing  
- resuming  

---

## 🏛 Architecture Diagram

<pre>
User
↓
StudyCoordinator
├── LLM Agent (Mock/Gemini-ready)
├── ContentSearchAgent
├── FlashcardAgent
├── LongRunningAgent
└── Session Service
</pre>

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

---

## 📁 Repository Structure

<pre>
├── README.md
├── LICENSE
├── requirements.txt
├── notebook/
│ └── smart_ai_study_assistant.ipynb
├── src/
│ ├── agents/
│ │ ├── llm_agent.py
│ │ ├── search_agent.py
│ │ ├── flashcard_agent.py
│ │ └── coordinator.py
│ ├── memory/
│ │ └── session_service.py
│ ├── models/
│ │ ├── learning_objective.py
│ │ ├── resource.py
│ │ └── flashcard.py
│ └── long_running_agent.py
└── assets/
└── architecture_diagram.png
</pre>

---

## 📄 Notebook

The full implementation and demo run are inside:


This notebook includes:
- step-by-step logic  
- agent orchestration  
- parallel execution demo  
- session memory handling  
- observability via logging  
- long-running agent pause/resume demonstration  

---

## 🛠 Technologies Used

- Python 3  
- Dataclasses  
- concurrent.futures  
- Logging (Observability)  
- Mock LLM Tool  
- In-memory session service  

No external API calls — fully offline.

---

## 🧪 Demo Output

The demo generates a full study plan across 5 topics:

- curated resources  
- LLM-powered flashcards  
- quizzes  
- prerequisites  
- key concepts  
- practice problems  
- session memory  
- agent logs  
- long-running agent output  

This demonstrates a working multi-agent system in action.

---

## 🔮 Future Enhancements

- Integrate real LLMs (Gemini/GPT)
- Add vector memory (FAISS/Chroma)
- Build a recommendation engine for next best topics
- Implement spaced repetition algorithms
- Add FastAPI backend or a Streamlit UI
- Build a prerequisite graph to generate learning paths

---

## 📜 License
MIT License

---

## 👤 Author
Your Name  
[Your GitHub Profile](#)

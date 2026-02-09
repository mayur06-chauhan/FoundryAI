# 🚀 FoundryAI — AI Startup Co-Founder

FoundryAI is an AI-powered platform that transforms raw startup ideas into structured execution plans.
It acts like a **technical co-founder**, helping founders move from idea to implementation using multi-agent AI workflows.

---

## 🌐 Live Demo

🔗 Deployed App link: 

---

## 📌 Problem Statement

Early-stage founders often have ideas but struggle with:

* Defining the problem clearly
* Planning MVP features
* Choosing the right tech stack
* Understanding market viability
* Creating a development roadmap

FoundryAI solves this by generating a complete project blueprint automatically.

---

## ✨ Features

* 🧠 Idea clarity detection
* ❓ Intelligent clarification questions
* 📋 MVP & future feature planning
* 🛣️ 6-week development roadmap
* ⚙️ Recommended modern tech stack
* 📊 Market analysis & monetization strategy
* 💾 Project saving using SQLite
* 🌐 Full-stack web interface

---

## 🏗️ Tech Stack

### Backend

* FastAPI
* LangChain
* LangGraph
* OpenAI API
* SQLAlchemy
* SQLite

### Frontend

* HTML
* CSS
* JavaScript

### Deployment

* Render (Free Cloud Hosting)

---

## 🧩 System Architecture

User Idea
→ Idea Agent (clarity check)
→ Product Agent (features)
→ Roadmap Agent
→ Tech Stack Agent
→ Market Agent
→ Save to Database

---

## 📂 Project Structure

```
FoundryAI/
│
├── main.py
├── requirements.txt
├── db/
├── agents/
├── workflow/
├── schemas/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
└── projects.db
```

---

## ⚙️ Local Setup

### 1. Clone Repository

```
git clone https://github.com/YOUR_USERNAME/FoundryAI.git
cd FoundryAI
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Add Environment Variable

Create `.env` file:

```
OPENAI_API_KEY=your_openai_api_key
```

### 4. Run Server

```
uvicorn main:app --reload
```

Open browser:

```
http://127.0.0.1:8000
```

---

## 🚀 Deployment (Render)

1. Push project to GitHub
2. Create Web Service on Render
3. Add environment variable:

```
OPENAI_API_KEY
```

4. Start command:
```
uvicorn main:app --host 0.0.0.0 --port 10000
```

---

## 🎯 Future Improvements
* User authentication
* PDF export
* Pitch deck generator
* Cost estimation
* Investor readiness score
* Multi-language support

---

## 👨‍💻 Author
Mayur Chauhan
BE — Artificial Intelligence & Data Science

---

## 📜 License
This project is for educational and demonstration purposes.

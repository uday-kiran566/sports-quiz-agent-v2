# 🏆 AI-Powered Sports Quiz Generator

An AI-powered Sports Quiz Generator built using **Streamlit**, **Google Gemini API**, **ChromaDB**, and **DuckDuckGo Search**. The application uses **Retrieval-Augmented Generation (RAG)** to generate context-aware multiple-choice sports quizzes from both historical facts and live web information.

---

## 🚀 Features

- 🏏 Select a Sport (Cricket, Football, Badminton)
- 🎯 Select Difficulty (Easy, Medium, Hard)
- 🧠 Uses ChromaDB Vector Database for historical facts
- 🌐 Retrieves live sports news using DuckDuckGo Search
- 🤖 Generates quizzes using Google Gemini API
- 📚 Uses Retrieval-Augmented Generation (RAG)
- ✅ Displays Correct Answers and Explanations
- 🔍 Shows the RAG Context used for quiz generation

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- ChromaDB
- DuckDuckGo Search
- python-dotenv

---

## 📂 Project Structure

```
sports-quiz-agent-v2/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── sports_facts.json
│
└── src/
    ├── config.py
    ├── database.py
    ├── generator.py
    ├── search.py
    └── __init__.py
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/uday-kiran566/sports-quiz-agent-v2.git
```

Go to the project folder:

```bash
cd sports-quiz-agent-v2
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it.

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```text
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run the Project

```bash
streamlit run app.py
```

---

## 🧠 RAG Workflow

```
User Input
      │
      ▼
Historical Facts (ChromaDB)
      │
      ▼
Live Sports News (DuckDuckGo)
      │
      ▼
Combined Context
      │
      ▼
Google Gemini API
      │
      ▼
Generated Sports Quiz
```

---

## 📸 Demo

Generate quizzes by selecting:

- Sport
- Difficulty

The application retrieves historical facts and live sports news, then generates multiple-choice quizzes with explanations.

---

## 👨‍💻 Author

**Uday Kiran**

B.Tech Computer Science and Engineering

AI-Powered Sports Quiz Generator Assignment
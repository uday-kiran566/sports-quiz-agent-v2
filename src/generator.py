from google import genai
from src.config import GEMINI_API_KEY
from src.database import query_historic_facts
from src.search import get_live_news_context


def compile_quiz_data(sport, difficulty):
    # Historical facts from ChromaDB
    db_query = f"{sport} history records championships rules"
    historic_facts = query_historic_facts(
        sport=sport,
        query_text=db_query,
        n_results=3
    )

    history_context = "\n".join(historic_facts)

    # Live news from DuckDuckGo
    live_news = get_live_news_context(sport)

    # Complete RAG Context
    rag_context = f"""
==========================
HISTORICAL FACTS
==========================
{history_context}

==========================
LATEST SPORTS NEWS
==========================
{live_news}
"""

    prompt = f"""
You are an expert Sports Quiz Generator.

Generate EXACTLY 4 multiple-choice questions.

Rules:
1. Use ONLY the information provided below.
2. Questions 1, 2 and 3 must come from Historical Facts.
3. Question 4 MUST come from Latest Sports News.
4. Each question must contain:
   - Question
   - Option A
   - Option B
   - Option C
   - Option D
   - Correct Answer
   - Explanation
5. Do not invent facts.
6. Format the output nicely.

Sport:
{sport}

Difficulty:
{difficulty}

Context:

{rag_context}
"""

    client = genai.Client(api_key=GEMINI_API_KEY)

    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=prompt
    )

    return response.text, rag_context
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

    # Live news
    live_news = get_live_news_context(sport)

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

Sport: {sport}
Difficulty: {difficulty}

Context:
{rag_context}
"""

    client = genai.Client(api_key=GEMINI_API_KEY)

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-lite",
            contents=prompt
        )

        return response.text, rag_context

    except Exception as e:
        print("Gemini API Error:", e)

        if sport.lower() == "cricket":
            sample_quiz = f"""
# 🏏 Cricket Sample Quiz ({difficulty})

**Gemini API is temporarily unavailable due to quota limits. Showing a sample quiz.**

## Question 1
Who is known as the "God of Cricket"?

A. Virat Kohli
B. MS Dhoni
C. Sachin Tendulkar
D. Ricky Ponting

**Correct Answer:** C. Sachin Tendulkar

**Explanation:** Sachin Tendulkar is widely known as the "God of Cricket".

---

## Question 2
How many players are there in a cricket team?

A. 9
B. 10
C. 11
D. 12

**Correct Answer:** C. 11

**Explanation:** A cricket team has 11 players.

---

## Question 3
Which country has won the ICC Cricket World Cup the most times?

A. India
B. England
C. Australia
D. Pakistan

**Correct Answer:** C. Australia

**Explanation:** Australia has won the ICC Cricket World Cup the most times.

---

## Question 4
Which trophy is played between India and Australia in Test cricket?

A. Asia Cup
B. Border-Gavaskar Trophy
C. Champions Trophy
D. Ashes

**Correct Answer:** B. Border-Gavaskar Trophy

**Explanation:** India and Australia compete for the Border-Gavaskar Trophy.
"""

        elif sport.lower() == "football":
            sample_quiz = f"""
# ⚽ Football Sample Quiz ({difficulty})

**Gemini API is temporarily unavailable due to quota limits. Showing a sample quiz.**

## Question 1
How many players are on the field for one football team?

A. 9
B. 10
C. 11
D. 12

**Correct Answer:** C. 11

**Explanation:** Each team has 11 players on the field.

---

## Question 2
Which country won the FIFA World Cup in 2022?

A. Brazil
B. France
C. Argentina
D. Germany

**Correct Answer:** C. Argentina

**Explanation:** Argentina won the 2022 FIFA World Cup.

---

## Question 3
Which player is known for winning eight Ballon d'Or awards?

A. Cristiano Ronaldo
B. Lionel Messi
C. Neymar
D. Luka Modrić

**Correct Answer:** B. Lionel Messi

**Explanation:** Lionel Messi has won eight Ballon d'Or awards.

---

## Question 4
How long is a regular football match?

A. 60 minutes
B. 70 minutes
C. 80 minutes
D. 90 minutes

**Correct Answer:** D. 90 minutes

**Explanation:** A regular match is 90 minutes plus added time.
"""

        else:
            sample_quiz = f"""
# 🏸 Badminton Sample Quiz ({difficulty})

**Gemini API is temporarily unavailable due to quota limits. Showing a sample quiz.**

## Question 1
How many players compete in a singles badminton match?

A. 1
B. 2
C. 4
D. 6

**Correct Answer:** B. 2

**Explanation:** Singles badminton is played between two players.

---

## Question 2
What is the object hit during a badminton match?

A. Ball
B. Shuttlecock
C. Disc
D. Puck

**Correct Answer:** B. Shuttlecock

**Explanation:** Badminton is played with a shuttlecock.

---

## Question 3
Which country is known for producing many top badminton players?

A. Australia
B. Indonesia
C. Canada
D. Spain

**Correct Answer:** B. Indonesia

**Explanation:** Indonesia has a strong badminton tradition.

---

## Question 4
What is the standard winning score in a badminton game?

A. 15
B. 18
C. 21
D. 25

**Correct Answer:** C. 21

**Explanation:** A game is normally played to 21 points.
"""

        return sample_quiz, rag_context
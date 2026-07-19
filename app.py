import streamlit as st
from src.generator import compile_quiz_data
from src.database import setup_and_populate_db


# Initialize database
@st.cache_resource
def load_database():
    setup_and_populate_db()


load_database()


# Page configuration
st.set_page_config(
    page_title="AI Sports Quiz Generator",
    page_icon="🏆",
    layout="centered"
)


# Title
st.title("🏆 AI-Powered Sports Quiz Generator")

st.write(
    "Generate engaging sports quizzes using AI, "
    "ChromaDB, and web search."
)


# Sidebar
st.sidebar.header("Quiz Settings")


sport_choice = st.sidebar.selectbox(
    "Select Sport",
    [
        "Cricket",
        "Football",
        "Badminton"
    ]
)


difficulty = st.sidebar.selectbox(
    "Select Difficulty",
    [
        "Easy",
        "Medium",
        "Hard"
    ]
)


# Generate button
if st.sidebar.button(
    "Generate Quiz",
    use_container_width=True
):

    with st.spinner("Generating quiz using RAG..."):

        try:

            quiz, context = compile_quiz_data(
                sport_choice,
                difficulty
            )


            st.success(
                "Quiz Generated Successfully!"
            )


            st.subheader(
                f"🏆 {sport_choice} Quiz ({difficulty})"
            )


            st.write(quiz)


            with st.expander(
                "🔍 View RAG Context"
            ):

                st.write(context)


        except Exception as e:

            st.markdown(quiz)(
                f"Error generating quiz: {e}"
            )
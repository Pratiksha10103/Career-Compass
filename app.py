import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from dotenv import load_dotenv
import google.generativeai as genai

# --- 1. CONFIGURATION & API SETUP ---
load_dotenv() 

# This is the "Bulletproof" logic:
# It looks for the key in Streamlit Secrets (Cloud) first,
# and falls back to your local .env file (Local) if not found.
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except (FileNotFoundError, KeyError):
    api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("API Key not found! Ensure it is in your .env file or Streamlit Cloud Secrets.")
    st.stop()

genai.configure(api_key=api_key)
# ... rest of your code .
model = genai.GenerativeModel("gemini-2.5-flash-lite")

# --- 2. AI ADVICE FUNCTION (INTEGRATED) ---
def get_ai_advice(user_name, user_skills, top_matches):
    """Fetches career guidance using your math-based top_matches as ground truth."""
    prompt = f"""
    You are an expert career counselor. 
    Student Name: {user_name}
    Skill Profile (1-10): {user_skills}
    
    My system calculated these top 3 career matches based on a weighted skill algorithm: {top_matches}.
    
    Please provide:
    1. A detailed validation of why these specific careers from my top matches fit the student.
    2. Suggest 2 alternative careers that align with these strengths but were not in the top 3.
    3. A 6-month learning roadmap.
    4. Expected entry-level salary ranges in INR.
    
    CRITICAL: You must use the provided 'top_matches' as the primary basis for your report. 
    Do not default to 'Data Analyst' unless the provided scores explicitly justify it.
    
    Format the output using professional Markdown with bold headers.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error connecting to AI: {e}"

# --- 3. STREAMLIT UI ---
st.set_page_config(page_title="AI Career Guidance", layout="wide")
st.title("🎓 AI Career Guidance Platform")
st.write("Find the best career based on your interests, skills, and strengths.")

name = st.text_input("Enter your name", placeholder="e.g. Pratiksha")

st.header("🧠 Skill & Interest Assessment (Rate 1–10)")
col1, col2, col3 = st.columns(3)

with col1:
    math = st.slider("Mathematics", 1, 10, 5)
    programming = st.slider("Programming", 1, 10, 5)
    data = st.slider("Data Analysis", 1, 10, 5)
    cybersecurity = st.slider("Cybersecurity", 1, 10, 5)
    physics = st.slider("Physics", 1, 10, 5)

with col2:
    biology = st.slider("Biology", 1, 10, 5)
    chemistry = st.slider("Chemistry", 1, 10, 5)
    finance = st.slider("Finance", 1, 10, 5)
    entrepreneurship = st.slider("Entrepreneurship", 1, 10, 5)
    management = st.slider("Management", 1, 10, 5)

with col3:
    creativity = st.slider("Design / Creativity", 1, 10, 5)
    writing = st.slider("Writing / Content Creation", 1, 10, 5)
    communication = st.slider("Communication", 1, 10, 5)
    leadership = st.slider("Leadership", 1, 10, 5)
    psychology = st.slider("Psychology", 1, 10, 5)

skills_dict = {
    "Math": math, "Programming": programming, "Data Analysis": data,
    "Cybersecurity": cybersecurity, "Physics": physics, "Biology": biology,
    "Chemistry": chemistry, "Finance": finance, "Entrepreneurship": entrepreneurship,
    "Management": management, "Creativity": creativity, "Writing": writing,
    "Communication": communication, "Leadership": leadership, "Psychology": psychology
}

career_weights = {
    "Software Engineer": {"Programming": 2, "Math": 1.5, "Data Analysis": 1},
    "Data Scientist": {"Programming": 2, "Data Analysis": 2, "Math": 1.5},
    "Cybersecurity Specialist": {"Cybersecurity": 2, "Programming": 1.5},
    "Doctor": {"Biology": 2, "Chemistry": 1.5},
    "Financial Analyst": {"Finance": 2, "Math": 1},
    "Startup Founder": {"Entrepreneurship": 2, "Leadership": 1.5, "Management": 1},
    "Content Creator": {"Creativity": 2, "Writing": 1.5, "Communication": 1},
    "Mechanical Engineer": {"Physics": 2, "Math": 1},
    "Psychologist": {"Psychology": 2, "Communication": 1},
    "Business Manager": {"Management": 2, "Leadership": 1.5, "Communication": 1}
}

# --- 4. CALCULATION & ACTION ---
if st.button("🔍 Analyze & Get AI Advice"):
    if not name:
        st.warning("Please enter your name first!")
    else:
        # Calculate Scores
        scores = {career: sum(skills_dict.get(skill, 0) * weight for skill, weight in weights.items()) 
                  for career, weights in career_weights.items()}
        
        top_careers = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]
        best_career = top_careers[0][0]

        st.success(f"✨ {name}, your best match based on math is **{best_career}**")

        # Visualizations Section
        st.divider()
        viz_col1, viz_col2 = st.columns(2)
        with viz_col1:
            st.subheader("📊 Skill Radar")
            labels = list(skills_dict.keys())
            values = list(skills_dict.values())
            angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
            values += values[:1]
            angles += angles[:1]
            fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
            ax.fill(angles, values, color='teal', alpha=0.3)
            ax.plot(angles, values, color='teal', linewidth=2)
            ax.set_thetagrids(np.degrees(angles[:-1]), labels)
            st.pyplot(fig)

        with viz_col2:
            st.subheader("🏆 Top Matches")
            score_df = pd.DataFrame(top_careers, columns=["Career", "Match Score"])
            st.bar_chart(score_df.set_index("Career"))

        # AI Advice Section
        st.divider()
        st.header("🤖 Personalized AI Counselor Report")
        with st.spinner("Gemini is validating your profile against the math model..."):
            # Passing your calculated results here!
            ai_report = get_ai_advice(name, skills_dict, top_careers)
            st.markdown(ai_report)

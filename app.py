##import streamlit as st
##import pandas as pd
##import matplotlib.pyplot as plt
##import numpy as np
##import os
##from dotenv import load_dotenv
##import google.generativeai as genai
##
### This is the line that actually reads the .env file
##load_dotenv() 
##print(f"DEBUG: My API Key is: {os.getenv('GOOGLE_API_KEY')}")
##api_key = os.getenv("GOOGLE_API_KEY")
##genai.configure(api_key=api_key)
####import os
####from dotenv import load_dotenv
####import google.generativeai as genai
####import os
####
####genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
####
####model = genai.GenerativeModel("gemini-1.5-pro-latest")
##def get_ai_advice(skills):
##    prompt = f"""
##    A student has the following skills: {skills}.
##    Suggest 5 suitable careers and explain why they fit.
##    """
##
##    response = model.generate_content(prompt)
##    return response.candidates[0].content.parts[0].text
##
##st.title("🎓 AI Career Guidance Platform")
##st.write("Find the best career based on your interests, skills, strengths, and weaknesses.")
##
##name = st.text_input("Enter your name")
##
##st.header("🧠 Skill & Interest Assessment (Rate 1–10)")
##
##col1, col2, col3 = st.columns(3)
##
##with col1:
##    math = st.slider("Mathematics",1,10)
##    programming = st.slider("Programming",1,10)
##    data = st.slider("Data Analysis",1,10)
##    cybersecurity = st.slider("Cybersecurity",1,10)
##    physics = st.slider("Physics",1,10)
##
##with col2:
##    biology = st.slider("Biology",1,10)
##    chemistry = st.slider("Chemistry",1,10)
##    finance = st.slider("Finance",1,10)
##    entrepreneurship = st.slider("Entrepreneurship",1,10)
##    management = st.slider("Management",1,10)
##
##with col3:
##    creativity = st.slider("Design / Creativity",1,10)
##    writing = st.slider("Writing / Content Creation",1,10)
##    communication = st.slider("Communication",1,10)
##    leadership = st.slider("Leadership",1,10)
##    psychology = st.slider("Psychology",1,10)
##
##skills = {
##"Math":math,
##"Programming":programming,
##"Data Analysis":data,
##"Cybersecurity":cybersecurity,
##"Physics":physics,
##"Biology":biology,
##"Chemistry":chemistry,
##"Finance":finance,
##"Entrepreneurship":entrepreneurship,
##"Management":management,
##"Creativity":creativity,
##"Writing":writing,
##"Communication":communication,
##"Leadership":leadership,
##"Psychology":psychology
##}
##
##career_data = {
##
##"Software Engineer":{
##"salary":"₹6L – ₹30L per year",
##"work_hours":"40-45 hrs/week",
##"description":"Develops software, applications, and systems."
##},
##
##"Data Scientist":{
##"salary":"₹8L – ₹35L per year",
##"work_hours":"40-45 hrs/week",
##"description":"Analyzes data to build predictive models."
##},
##
##"Cybersecurity Specialist":{
##"salary":"₹7L – ₹28L per year",
##"work_hours":"40-50 hrs/week",
##"description":"Protects systems and networks from cyber threats."
##},
##
##"Doctor":{
##"salary":"₹8L – ₹25L per year",
##"work_hours":"50-60 hrs/week",
##"description":"Diagnoses and treats patients."
##},
##
##"Financial Analyst":{
##"salary":"₹6L – ₹20L per year",
##"work_hours":"40-50 hrs/week",
##"description":"Analyzes financial data and investment opportunities."
##},
##
##"Startup Founder":{
##"salary":"Varies widely",
##"work_hours":"50-70 hrs/week",
##"description":"Builds and manages a startup business."
##},
##
##"Content Creator":{
##"salary":"₹3L – ₹20L+ per year",
##"work_hours":"Flexible",
##"description":"Creates online content such as videos and media."
##},
##
##"Mechanical Engineer":{
##"salary":"₹5L – ₹18L per year",
##"work_hours":"40-45 hrs/week",
##"description":"Designs machines and mechanical systems."
##},
##
##"Psychologist":{
##"salary":"₹4L – ₹15L per year",
##"work_hours":"35-45 hrs/week",
##"description":"Studies human behavior."
##},
##
##"Business Manager":{
##"salary":"₹6L – ₹22L per year",
##"work_hours":"40-50 hrs/week",
##"description":"Manages teams and business operations."
##}
##
##}
##
##career_weights = {
##
##"Software Engineer":{"Programming":2,"Math":1.5,"Data Analysis":1},
##
##"Data Scientist":{"Programming":2,"Data Analysis":2,"Math":1.5},
##
##"Cybersecurity Specialist":{"Cybersecurity":2,"Programming":1.5},
##
##"Doctor":{"Biology":2,"Chemistry":1.5},
##
##"Financial Analyst":{"Finance":2,"Math":1},
##
##"Startup Founder":{"Entrepreneurship":2,"Leadership":1.5,"Management":1},
##
##"Content Creator":{"Creativity":2,"Writing":1.5,"Communication":1},
##
##"Mechanical Engineer":{"Physics":2,"Math":1},
##
##"Psychologist":{"Psychology":2,"Communication":1},
##
##"Business Manager":{"Management":2,"Leadership":1.5,"Communication":1}
##
##}
##
##if st.button("🔍 Analyze My Career"):
##
##    scores = {}
##
##    for career, weights in career_weights.items():
##
##        score = 0
##
##        for skill, weight in weights.items():
##            score += skills.get(skill,0) * weight
##
##        scores[career] = score
##
##    sorted_careers = sorted(scores.items(), key=lambda x: x[1], reverse=True)
##    top_careers = sorted_careers[:3]
##
##    best_career = top_careers[0][0]
##
##    st.success(f"✨ {name}, your best career match is **{best_career}**")
##
##    info = career_data[best_career]
##
##    col1,col2 = st.columns(2)
##
##    with col1:
##        st.metric("💰 Salary",info["salary"])
##
##    with col2:
##        st.metric("⏰ Work Hours",info["work_hours"])
##
##    st.write("### 📖 Career Description")
##    st.write(info["description"])
##
##    st.header("🏆 Top Career Matches")
##
##    for c,score in top_careers:
##        st.write(f"**{c}** — Match Score: {round(score,1)}")
##
##    st.header("📊 Career Match Scores")
##
##    score_df = pd.DataFrame(scores.items(), columns=["Career","Score"])
##
##    fig3, ax3 = plt.subplots()
##    ax3.bar(score_df["Career"], score_df["Score"])
##    plt.xticks(rotation=45)
##    st.pyplot(fig3)
##
##    strengths = [k for k,v in skills.items() if v >= 8]
##    moderate = [k for k,v in skills.items() if 5 <= v < 8]
##    weaknesses = [k for k,v in skills.items() if v <= 4]
##
##    st.header("🧠 Skill Analysis")
##
##    col1,col2,col3 = st.columns(3)
##
##    with col1:
##        st.subheader("💪 Strong Areas")
##        for s in strengths:
##            st.write("✅",s)
##
##    with col2:
##        st.subheader("📊 Average Areas")
##        for m in moderate:
##            st.write("➖",m)
##
##    with col3:
##        st.subheader("⚠ Needs Improvement")
##        for w in weaknesses:
##            st.write("❗",w)
##
##    st.header("📊 Skill Radar Chart")
##
##    labels=list(skills.keys())
##    values=list(skills.values())
##
##    angles=np.linspace(0,2*np.pi,len(labels),endpoint=False)
##    values=np.concatenate((values,[values[0]]))
##    angles=np.concatenate((angles,[angles[0]]))
##
##    fig=plt.figure()
##    ax=fig.add_subplot(111,polar=True)
##
##    ax.plot(angles,values)
##    ax.fill(angles,values,alpha=0.25)
##
##    ax.set_thetagrids(angles[:-1]*180/np.pi,labels)
##    ax.set_ylim(0,10)
##
##    st.pyplot(fig)
##
##    st.header("🥧 Skill Distribution")
##
##    df = pd.DataFrame(list(skills.items()), columns=["Skill","Score"])
##
##    fig2, ax2 = plt.subplots()
##    ax2.pie(df["Score"],labels=df["Skill"],autopct="%1.1f%%",startangle=90)
##    ax2.axis("equal")
##
##    st.pyplot(fig2)
##
##    st.header("📚 Skills to Improve")
##
##    for w in weaknesses:
##        st.write(f"Improve your **{w}** through courses or practice.")
##
##def get_ai_advice(skills):
##
##    prompt = f"""
##You are an expert career counselor.
##
##Student skill profile:
##{skills}
##
##Provide:
##
##1. Top 5 career options
##2. Why each career suits the student
##3. Student strengths
##4. Skill gaps
##5. A 6 month learning roadmap
##6. Salary expectations
##"""
##
##    response = model.generate_content(prompt)
##    return response.text
##
##st.header("🤖 AI Career Advice")
##
##if st.button("Get AI Advice"):
##
##    with st.spinner("AI analyzing your profile..."):
##
##        advice = get_ai_advice(skills)
##
##    st.write(advice)
##
##
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from dotenv import load_dotenv
import google.generativeai as genai

# --- 1. CONFIGURATION & API SETUP ---
load_dotenv() 
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("API Key not found! Please check your .env file.")
    st.stop()

genai.configure(api_key=api_key)

# Initialize the model globally so the function can see it
# Change from gemini-2.0-flash to gemini-2.5-flash-lite
model = genai.GenerativeModel("gemini-2.5-flash-lite")
# OR use the very latest
# model = genai.GenerativeModel("gemini-3.0-flash")
# --- 2. AI ADVICE FUNCTION ---
def get_ai_advice(user_name, user_skills):
    """Fetches career guidance from Gemini based on user skills."""
    prompt = f"""
    You are an expert career counselor. 
    The student's name is {user_name}.
    Student skill profile (rated 1-10):
    {user_skills}

    Please provide:
    1. Top 5 career options with a brief 'Why it fits'.
    2. A summary of their top 3 strengths.
    3. The most critical 'Skill Gap' they should focus on.
    4. A high-level 6-month learning roadmap.
    5. Expected entry-level salary ranges in INR.
    
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

# Store skills in a dictionary
skills_dict = {
    "Math": math, "Programming": programming, "Data Analysis": data,
    "Cybersecurity": cybersecurity, "Physics": physics, "Biology": biology,
    "Chemistry": chemistry, "Finance": finance, "Entrepreneurship": entrepreneurship,
    "Management": management, "Creativity": creativity, "Writing": writing,
    "Communication": communication, "Leadership": leadership, "Psychology": psychology
}

# --- 4. HARDCODED LOGIC (FOR CHARTS) ---
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

# --- 5. ACTION BUTTON ---
if st.button("🔍 Analyze & Get AI Advice"):
    if not name:
        st.warning("Please enter your name first!")
    else:
        # Calculate Scores
        scores = {}
        for career, weights in career_weights.items():
            score = sum(skills_dict.get(skill, 0) * weight for skill, weight in weights.items())
            scores[career] = score

        top_careers = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]
        best_career = top_careers[0][0]

        st.success(f"✨ {name}, your best career match is **{best_career}**")

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
        with st.spinner("Gemini is analyzing your profile..."):
            ai_report = get_ai_advice(name, skills_dict)
            st.markdown(ai_report)

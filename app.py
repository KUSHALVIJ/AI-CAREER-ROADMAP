# ================= STEP 1: IMPORT MODULES =================

import os
import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# ================= STEP 2: PAGE CONFIGURATION =================

st.set_page_config(
  page_title="AI Career Roadmap Generator",
  page_icon="🚀",
  layout="wide")

st.title("🚀 AI Career Roadmap Generator")

st.markdown("""
Generate a **personalized career roadmap** using **Google Gemini + LangChain**.
Receive AI-powered guidance based on your skills, interests, education, and career goals.
""")

col1, col2, col3 = st.columns(3)

with col1:
  st.metric("🤖 AI Model", "Gemini")

with col2:
  st.metric("🧠 Framework", "LangChain")

with col3:
  st.metric("📄 Output", "Career Roadmap")

  st.sidebar.title("⚙️ Configuration")

# ================= STEP 3: API KEY =================

GOOGLE_API_KEY = st.sidebar.text_input(
  "Enter your Gemini API Key",
  type="password")

if GOOGLE_API_KEY:
  os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# ================= STEP 4: USER INPUT FORM =================

left_col, right_col = st.columns([1, 1])
with left_col:
  with st.form("career_form"):
    name = st.text_input("👤 Full Name")
    qualification = st.selectbox(
      "🎓 Highest Qualification",
      [
      "10th",
      "12th",
      "Diploma",
      "BCA",
      "B.Tech",
      "B.Sc",
      "MCA",
      "MBA",
      "Other"])
    
    
    experience = st.text_input("💼 Current Year / Experience")
    skills = st.text_area(
    "💻 Current Skills",
    placeholder="Example: Python, SQL, Excel")
    
    
    interests = st.text_area(
      "❤️ Interests",
      placeholder="Example: AI, Data Science, Web Development")
    
    career = st.selectbox(
      "🎯 Dream Career",
      [
      "AI Engineer",
      "Data Scientist",
      "Software Developer",
      "Cyber Security Analyst",
      "Cloud Engineer",
      "Business Analyst",
      "UI/UX Designer",
      "Full Stack Developer",
      "Other"])
    
    time = st.slider(
      "⏰ Study Hours Per Week",
      min_value=1,
      max_value=40,
      value=10)
    
    generate = st.form_submit_button("🚀 Generate Career Roadmap")

# ================= STEP 5: INITIALIZE GEMINI =================

if GOOGLE_API_KEY:
  
  llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

# ================= STEP 6: CREATE PROMPT TEMPLATE =================

prompt = ChatPromptTemplate.from_template("""

You are an expert AI Career Counselor.
Analyze the user's profile and generate a personalized career roadmap.

User Details:

Name: {name}
Highest Qualification: {qualification}
Current Year/Experience: {experience}
Current Skills: {skills}
Interests: {interests}
Dream Career: {career}
Available Study Time per Week: {time}

Generate a well-structured report with the following sections:

1. Career Summary
2. Current Strengths
3. Skill Gap Analysis
4. Skills to Learn
5. Recommended Certifications
6. Recommended Projects
7. Free Learning Resources
   (YouTube Channels, Websites, Documentation)
8. 6-Month Learning Roadmap
9. Career Opportunities
10. Final AI Advice

Make the response practical, detailed, and beginner-friendly.
Use bullet points wherever possible.
""")

# ================= STEP 7: CREATE LCEL CHAIN =================

chain = (prompt| llm| StrOutputParser())

# ================= STEP 8: GENERATE CAREER ROADMAP =================

if generate:
  if not GOOGLE_API_KEY:
    st.error("⚠️ Please enter your Gemini API Key.")
  else:
    if (
      not name or
      not experience or
      not skills or
      not interests):
        
        st.warning("⚠️ Please fill all the required fields.")
    else:
      with st.spinner("🚀 Generating your personalized career roadmap..."):
        
        
        
        try:
          response = chain.invoke({
          "name": name,
          "qualification": qualification,
          "experience": experience,
          "skills": skills,
          "interests": interests,
          "career": career,
          "time": f"{time} Hours per Week"})
          
          
          with right_col:
            st.success("✅ Career Roadmap Generated Successfully!")
          st.subheader("📄 Your Personalized Career Roadmap")
          st.markdown(response)
          
          st.download_button(
          label="📥 Download Career Roadmap",
          data=response,
          file_name="Career_Roadmap.txt",
          mime="text/plain")
        
        except Exception as e:
          st.error(f"❌ Error: {e}")


# ================= STEP 9: DOWNLOAD BUTTON =================

st.download_button(
  label="📥 Download Career Roadmap",
  data=response,
  file_name="Career_Roadmap.txt",
  mime="text/plain")

# ================= STEP 10: FOOTER =================

st.markdown("---")

st.markdown(
    """<div style='text-align: center; color: gray;'>
    🚀 AI Career Roadmap Generator <br>
    Built using <b>Streamlit</b>, <b>LangChain</b> and <b>Google Gemini</b>
    </div>
    """,unsafe_allow_html=True)
























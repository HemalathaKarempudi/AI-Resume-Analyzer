import streamlit as st
import PyPDF2

st.title("AI Resume Analyzer")

skills = ["python","machine learning","data analysis",
          "sql","power bi","deep learning","excel"]

uploaded_file = st.file_uploader("Upload Resume (PDF)",type=["pdf"])

def extract_text(file):
    reader = PyPDF2.PdfReader(file)
    text=""
    for page in reader.pages:
        text+=page.extract_text()
    return text

if uploaded_file:
    
    resume_text = extract_text(uploaded_file)
    
    found_skills = []
    
    for skill in skills:
        if skill.lower() in resume_text.lower():
            found_skills.append(skill)
    
    score = (len(found_skills)/len(skills))*100
    
    st.subheader("Skills Found")
    st.write(found_skills)
    
    st.subheader("Resume Score")
    st.write(score)
    
    missing = list(set(skills)-set(found_skills))
    
    st.subheader("Skills to Improve")
    st.write(missing)
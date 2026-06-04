import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
from PyPDF2 import PdfReader
import io
import http.client
import json

# --- 1. GLOBAL INITIALIZATION & CONFIG ---
st.set_page_config(page_title="AI Job Market Intelligence 2026", layout="wide", page_icon="📈")

# Aapki original, verified AQ wali key
API_KEY = "enter your api key here"

# --- 2. SQL DATA RETRIEVAL FUNCTION ---
def fetch_sql_data():
    conn = sqlite3.connect("jobs_market.db")
    query = "SELECT * FROM job_postings"
    df_data = pd.read_sql_query(query, conn)
    conn.close()
    return df_data

# Load data from database backend
try:
    df = fetch_sql_data()
except Exception as e:
    st.error("Could not read SQL Database. Please run 'db_setup.py' first.")
    df = pd.DataFrame()

# --- 3. DASHBOARD USER INTERFACE ---
tab1, tab2 = st.tabs(["📊 Market Analytics Dashboard", "🤖 AI Resume Skill-Gap Analyzer"])

# --- TAB 1: DATA VISUALIZATION (SQL BACKEND) ---
with tab1:
    st.title("📈 Tech Job Market Insights")
    st.markdown("Real-time job distribution and analytics queried straight from your local SQL database.")
    
    if not df.empty:
        # Dynamic Metric Indicators
        m1, m2, m3 = st.columns(3)
        m1.metric("Total Positions Tracked", len(df))
        m2.metric("Highest Package Offered", f"₹{df['Salary_INR_LPA'].max()} LPA")
        m3.metric("Top Hiring Location", df['Location'].value_counts().index[0])
        
        st.markdown("---")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("📋 Active Openings Schema View")
            st.dataframe(df, use_container_width=True)
            
        with col2:
            st.subheader("💰 CTC Ranges by Job Profile")
            fig = px.bar(df, x="Job_Title", y="Salary_INR_LPA", color="Location", 
                         title="Salary Analysis (LPA)", barmode="group", text_auto=True)
            st.plotly_chart(fig, use_container_width=True)

# --- TAB 2: INTERACTIVE AI AGENT FEATURE ---
with tab2:
    st.title("🤖 AI-Driven Skill-Gap Advisor")
    st.markdown("Upload your professional profile to analyze your readiness against competitive market requirements.")
    
    target_job = st.selectbox("Select Your Desired Career Path:", ["Data Analyst", "Senior Data Analyst", "Power BI Developer", "AI Engineer"])
    uploaded_file = st.file_uploader("Drop your Resume here (PDF format only)", type=["pdf"])
    
    if uploaded_file is not None:
        with st.spinner("AI parsing engine processing document text..."):
            
            # Extract raw string text from PDF stream
            pdf_reader = PdfReader(io.BytesIO(uploaded_file.read()))
            resume_text = ""
            for page in pdf_reader.pages:
                text = page.extract_text()
                if text:
                    resume_text += text
            
            # Construct strict industrial prompt blueprint
            prompt = f"""
            You are a premier technical recruitment auditor specializing in data and software domains.
            Audit the following resume text against the specific role requirements of a '{target_job}'.
            
            Structure your output cleanly with these markdown sections:
            ### 📊 Profile Match Score
            [Provide a realistic percentage rating out of 100%]
            
            ### ✅ Core Strengths Validated
            [List strong technical keywords, projects, or concepts found matching the role]
            
            ### ⚠️ Identified Skill Gaps
            [Detail missing critical technical tools, advanced libraries, or domain competencies required for this role]
            
            ### 🗺️ Next-Step Actionable Upskilling Roadmap
            [Provide a precise, 3-step learning track to optimize the candidate's profile]
            
            Resume Text:
            {resume_text}
            """
            
            # --- COMBINED BULLETPROOF NETWORK ROUTE ---
            try:
                # Public global domain address (Isme getaddrinfo network error nahi aayega)
                conn = http.client.HTTPSConnection("generativelanguage.googleapis.com")
                
                payload = json.dumps({
                    "contents": [{
                        "parts": [{
                            "text": prompt
                        }]
                    }]
                })
                
                headers = {
                    'Content-Type': 'application/json'
                }
                
                # Naye format key ke liye exact specific beta layout parameters
                url_endpoint = f"/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
                
                conn.request("POST", url_endpoint, payload, headers)
                res = conn.getresponse()
                data = res.read()
                
                response_json = json.loads(data.decode("utf-8"))
                
                # Check and display final clean output
                if 'candidates' in response_json:
                    ai_response_text = response_json['candidates'][0]['content']['parts'][0]['text']
                    st.success("Profile Auditing Completed!")
                    st.markdown("---")
                    st.markdown(ai_response_text)
                else:
                    st.error(f"Google Server Context Response: {response_json}")
                    
            except Exception as e:
                st.error(f"Execution Error: Verification failed. Code details: {e}")

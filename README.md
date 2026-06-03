# 📈 Intelligent Job Market Analytics Dashboard & AI Resume Auditor

A dynamic, full-stack Data Intelligence application built to bridge the gap between active tech market demands and professional profiles. This project features a dual-engine architecture: a local **SQL-driven analytics dashboard** tracking live CTC ranges and job volumes, paired with an interactive **AI Skill-Gap Advisor** powered by advanced LLM inference layers.

---

## 🚀 Key Features

### 📊 1. Market Analytics Dashboard
* **Live SQL Backend:** Queries real-time job distribution and industry schema straight from a local SQLite database (`jobs_market.db`).
* **Interactive Visualizations:** Leverages Plotly Express to render dynamic multi-timeframe analytics, including corporate package distributions (LPA) grouped by top geographical tech hubs.
* **Key Metric Indicators:** Provides at-a-glance data insights on total tracked positions, peak industry CTCs, and primary hiring locations.

### 🤖 2. Intelligent AI Skill-Gap Advisor
* **Automated PDF Parsing:** Integrated parsing layer utilizing `PyPDF2` to extract clean textual metadata streams directly from raw candidate resumes.
* **Intelligent Profile Auditing:** Executes an advanced system prompt targeting core tech competencies for specialized roles like *Data Analyst, Senior Data Analyst, Power BI Developer, and AI Engineer*.
* **Deep Evaluation Blueprint:** Leverages secure API gateways via the standard Python `requests` pipeline to deliver immediate, structured recruitment insights:
  * Profile Match Score (Realistic Percentage Index)
  * Validated Technical Core Strengths
  * Identified Technical & Tooling Skill Gaps
  * Step-by-Step Actionable Learning & Upskilling Roadmap

---

## 🛠️ Tech Stack & Architecture

* **Front-End Framework:** Streamlit (Python-based Interactive Web UI)
* **Database Layer:** SQLite3 (Relational Schema Database Engine)
* **Data Processing & Viz:** Pandas & Plotly Express
* **AI Model Pipeline:** Secure REST API Cloud Connection Endpoints
* **Deployment/Tunneling Utilities:** PyNgrok for dynamic external network access tunneling

---

## 💻 Setup & Installation Instructions

Follow these precise steps to deploy and run this repository locally on your machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/AI-Job-Market-Intelligence.git](https://github.com/YOUR_USERNAME/AI-Job-Market-Intelligence.git)
cd AI-Job-Market-Intelligence

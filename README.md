# 📰 NYTimes Analytics Dashboard  

An interactive **Dash web application** that analyzes New York Times articles with powerful search, trend visualizations, and insights.  
The project also includes **automated data pipelines** powered by GitHub Actions to keep datasets fresh and up-to-date.  

<img width="1909" height="947" alt="Image" src="https://github.com/user-attachments/assets/e5b33761-68d1-4fa3-bdc3-3e84414bebe3" />

<img width="1909" height="947" alt="Image" src="https://github.com/user-attachments/assets/9455cab1-9100-4b36-96bf-da1a66227e12" />



---

## 🚀 Features  

- **📊 Interactive Dash App**  
  - Search across articles using multi-word queries.  
  - Explore publication trends over time.  
  - Browse a carousel of the most-viewed articles from the past 30 days.  
  - Responsive layout built with **Dash + Bootstrap**.  

- **⚙️ Automated Data Pipelines**  
  - Two **GitHub Actions workflows**:  
    - Weekly updates to fetch the latest datasets.  
    - Monthly updates to fetch and append new archives.  
  - Pipelines store cleaned data in both **Parquet** and **CSV** formats.  

- **📂 Clean Project Structure**  
  - `app.py`: Main Dash application.  
  - `components/`: Modularized UI and logic (charts, navbar, search section, etc.).  
  - `datasets/`: Processed NYT datasets.  
  - `.github/workflows/`: GitHub Actions configs for automated pipelines.  

- **🔍 Search Mechanism**  
  - Built a **search_text** index combining headline, abstract, and keywords.  
  - Supports multi-word queries like `"black box"` to return relevant matches.  

---

## 🛠️ Tech Stack  

- [Dash](https://dash.plotly.com/) (Frontend + Backend)  
- [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/) (Styling)  
- [Pandas](https://pandas.pydata.org/) & [PyArrow](https://arrow.apache.org/) (Data processing)  
- [Plotly](https://plotly.com/python/) (Charts)  
- [GitHub Actions](https://docs.github.com/en/actions) (CI/CD workflows)  

---

## ⚡ Getting Started  

Clone the repository:  
```bash
git clone https://github.com/Dashboard-Design/nyt-articles-dashboard.git
cd nyt-articles-dashboard
```

Create a virtual environment (using uv or venv):
```bash
uv venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

Install dependencies:
```bash
uv pip install -r requirements.txt
```

Run the app:
```bash
uv run app.py
```
The app will be available at:
👉 http://127.0.0.1:8050

---

- ## 🔄 Automated Workflows
  - Weekly Workflow: Fetches NYT’s most-viewed articles (last 30 days).
  - Monthly Workflow: Downloads and appends the latest archive.
 
---

- ## 👨‍💻 About

This project was developed by Sajjad Ahmadi
as part of my exploration into data visualization, automation, and web dashboards.

I started this project to:
  - Learn how to build production-ready data pipelines with GitHub Actions.
  - Explore large-scale text datasets and how to search/filter them efficiently.
  - Develop a clean, scalable Dash app that can evolve with new features.

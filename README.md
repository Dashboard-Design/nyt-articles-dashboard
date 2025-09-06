# 📰 NYTimes Analytics Dashboard  

An interactive **Dash web application** that analyzes New York Times articles with powerful search, trend visualizations, and insights.  
The project also includes **automated data pipelines** powered by GitHub Actions to keep datasets fresh and up-to-date.  

![Dashboard Screenshot](assets/dashboard_preview.png) <!-- Replace with actual screenshot -->

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

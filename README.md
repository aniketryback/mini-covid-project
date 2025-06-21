# 🧪 Mini COVID ETL Project (Python + Pandas)

This is a simple, real-world ETL (Extract, Transform, Load) project built in pure Python. It downloads live COVID-19 data, cleans and filters it, and generates a bar chart of the top vaccinated countries — all without using any cloud or orchestration tools.

---

## 🔧 Tech Stack

- Python 3.10+  
- Pandas  
- Matplotlib  

---

## 📦 What This Project Does

| Step | Description |
|------|-------------|
| ✅ Extract | Downloads latest COVID-19 data from [Our World in Data](https://ourworldindata.org/) |
| ✅ Transform | Selects relevant columns, drops nulls, and filters rows |
| ✅ Load | Saves cleaned and filtered CSVs into `output/` folder |
| ✅ Visualize | Plots a horizontal bar chart of top 10 vaccinated countries |

---

## 🧠 Files & Folders
mini-covid-project/
- covid_etl.py          <- main Python ETL script
- output/               <- folder for saved data + chart
  - covid_cleaned.csv
  - vaccinated_over_10m.csv
  - top10_vaccinated.png

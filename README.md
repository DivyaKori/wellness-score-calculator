# Wellness Score Calculator 

This project calculates a daily **Wellness Score (0–100)** based on
sleep hours, steps walked, and mood ratings using Python.
It also visualizes wellness trends using line graphs.

---

##  Project Objective
To design a simple yet effective scoring algorithm that converts
daily wellness data into a single meaningful score and analyzes trends over time.

---

## 📂 Dataset
The dataset (`wellness_data_300_rows.csv`) contains 300 daily records with:
- Date
- Sleep Hours (hours/day)
- Steps Walked (count/day)
- Mood Rating (1–5)

---

## ⚙️ Wellness Score Calculation
The wellness score is calculated using weighted normalization:

- Sleep Score → 40%
- Steps Score → 35%
- Mood Score → 25%

Each value is normalized and combined into a final score between **0 and 100**.

---

##  Visualizations
The project generates:
1. **Wellness Score over Time (Line Graph)**
2. **Steps vs Wellness Score (Line Graph)**

Graphs are interactive — hovering over points displays `(Date, Score)` or `(Steps, Score)`.

---

## 🛠️ Technologies Used
- Python
- Pandas
- Matplotlib
- VS Code
- Git & GitHub

---

## 🚀 How to Run the Project

1. Install required libraries:
   ```bash
   pip install pandas matplotlib

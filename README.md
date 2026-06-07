# 📊 Sales Demand Forecasting & Analytics Dashboard

An end-to-end Data Science project that performs **Exploratory Data Analysis (EDA)** and **Revenue Prediction** using Machine Learning, with an interactive **Streamlit Dashboard**.

---

## 🚀 Live Demo
Run locally using the steps below.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.14 | Core Language |
| Pandas & NumPy | Data Processing |
| Matplotlib & Seaborn | Data Visualization |
| Scikit-learn | Machine Learning |
| Streamlit | Interactive Dashboard |
| Jupyter Notebook | EDA & Analysis |
| Plotly | Interactive Charts |

---

## 📁 Project Structure

```
sales-demand-forecasting/
├── data/
│   └── sales_data.csv          # 1000-row sales dataset
├── notebooks/
│   └── EDA_and_Modeling.ipynb  # Full EDA + ML notebook
├── app/
│   └── app.py                  # Streamlit dashboard
├── models/
│   └── model.pkl               # Trained Random Forest model
└── requirements.txt
```

---

## ✨ Features

- 📈 **Exploratory Data Analysis** — trends, distributions, correlations
- 🗺️ **Regional & Category Analysis** — revenue breakdown by region and product category
- 📅 **Monthly Revenue Trends** — time series visualization
- 🤖 **ML Revenue Predictor** — predict revenue using Random Forest (R² = 0.9884)
- 🔍 **Interactive Filters** — filter by category, region, and year
- 📊 **Correlation Heatmap** — feature relationships

---

## 🧠 ML Models Used

| Model | MAE | R² Score |
|-------|-----|----------|
| Linear Regression | - | ~0.97 |
| Random Forest | - | **0.9884** ✅ |

**Best Model: Random Forest Regressor** with 98.84% accuracy

---

## ⚙️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Vyshali22/sales-demand-forecasting.git
cd sales-demand-forecasting
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Jupyter Notebook (EDA)
```bash
jupyter notebook notebooks/EDA_and_Modeling.ipynb
```

### 4. Run Streamlit Dashboard
```bash
streamlit run app/app.py
```

---

## 📸 Dashboard Preview

- Key Metrics: Total Revenue, Orders, Avg Order Value, Avg Discount
- Revenue by Category & Region
- Monthly Revenue Trend
- Top 10 Products
- Live Revenue Predictor

---

## 👩‍💻 Author

**Vyshali** — Fresher | Python | Data Science | Java | Spring Boot  
📍 Hyderabad, India  
🔗 [GitHub](https://github.com/Vyshali22) | [LinkedIn](https://linkedin.com/in/vyshali22)
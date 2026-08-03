# Delivery Delay Risk Analysis

Analyzing 180K+ shipments to uncover why 55% of deliveries are late — KPIs, regional risk diagnostics, and a live Streamlit dashboard.

## 📌 Project Overview

**Client:** APL Logistics (KWE Group) | **Program:** Unified Mentor

APL Logistics handles high-volume, multi-region shipments. Despite detailed order and shipping data, the organization lacked clear visibility into on-time vs delayed deliveries, why shipments are delayed, and which regions/shipping modes carry the highest risk.

This project builds a diagnostic intelligence layer — moving logistics teams from reactive firefighting to data-driven operational control.

## 📂 Dataset

- **Source:** DataCo Supply Chain Dataset
- **Size:** 180,519 orders × 40 columns
- **Encoding:** latin-1
- **Key fields:** shipping duration (real vs scheduled), delivery status, late delivery risk, shipping mode, customer segment, order region/market, sales & profit metrics

## ✅ Progress So Far

### Step 1: Data Cleaning & Validation
- Validated shipping duration values (0 invalid/negative rows found)
- Removed missing/duplicate critical records (0 removed — dataset was clean)
- Flagged 7,754 cancelled shipments (excluded from delay analysis, retained for order-status analysis)
- Standardized region & market naming (fixed casing/whitespace, preserved acronyms like USCA, LATAM, USA)
- **Result:** 100% of records retained after validation (180,519 rows)

### Step 2: Delivery Gap Calculation
- Computed `Delay_Gap = Days for shipping (real) − Days for shipment (scheduled)`
- Classified every order as **On-time**, **Delayed**, or **Early**

### Step 3: Overall Delivery Performance Analysis
| Metric | Value |
|---|---|
| On-Time Delivery Rate | **18.70%** |
| Late Delivery Risk Ratio | **54.83%** |
| Average Delivery Delay | **0.57 days** |

### Step 4: Shipping Mode Efficiency Analysis *(in progress)*
- Comparing average delay gap and SLA compliance across shipping modes
- Early finding: Standard Class is the most reliable mode; Second Class runs ~2 days over schedule on average

## 🔜 Remaining Steps
- Step 5: Regional & Market Diagnostics
- Step 6: Customer Segment Impact Analysis
- Streamlit dashboard (4 modules: Delivery Performance Overview, Delay Risk Analysis, Shipping Mode Comparison, Regional/Market Heatmaps)
- Research paper (EDA, insights, recommendations)
- Executive summary for stakeholders

## 🛠️ Tech Stack
- Python, Pandas, NumPy
- Matplotlib / Plotly / Seaborn (EDA & charts)
- Streamlit (interactive dashboard)
- Jupyter Notebook (analysis workflow)

## 📁 Repo Structure
```
├── data/
│   └── APL_Logistics.csv          # raw dataset (not included — see Dataset section)
├── notebooks/
│   └── analysis.ipynb             # step-by-step cleaning, KPI, and EDA notebook
├── step1_cleaned_data.csv         # cleaned dataset output
├── app.py                         # Streamlit dashboard (coming soon)
└── README.md
```

## ▶️ How to Run
```bash
pip install pandas numpy streamlit plotly matplotlib seaborn

# Run analysis notebook
jupyter notebook notebooks/analysis.ipynb

# Run dashboard (once built)
streamlit run app.py
```

## 📊 Key KPIs Tracked
- On-Time Delivery Rate (%)
- Average Delivery Delay (Days)
- Late Delivery Risk Ratio
- Shipping Mode Efficiency Index
- Regional Delay Index

---
*This is an active work-in-progress project. README will be updated as each analysis step is completed.*

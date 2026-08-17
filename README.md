# Delivery Delay Risk Analysis

Analyzing 180K+ shipments to uncover why 55% of deliveries are late — KPIs, regional risk diagnostics, and a live Streamlit dashboard.

## 📌 Project Overview

**Client:** APL Logistics (KWE Group)

APL Logistics handles high-volume, multi-region shipments. Despite detailed order and shipping data, the organization lacked clear visibility into on-time vs delayed deliveries, why shipments are delayed, and which regions/shipping modes carry the highest risk.

This project builds a diagnostic intelligence layer — moving logistics teams from reactive firefighting to data-driven operational control.

## 🔗 Live Dashboard
👉 [View the deployed app](http://localhost:8501/)

## 📂 Dataset

- **Source:** DataCo Supply Chain Dataset
- **Size:** 180,519 orders × 40 columns
- **Encoding:** latin-1
- **Key fields:** shipping duration (real vs scheduled), delivery status, late delivery risk, shipping mode, customer segment, order region/market, sales & profit metrics
- **Note:** dataset does not include order/shipping date fields — synthetic dates were generated for the dashboard's date range filter (clearly labeled as simulated)

## ✅ Methodology & Findings

### 1. Data Cleaning & Validation
- Validated shipping duration values (0 invalid/negative rows found)
- Removed missing/duplicate critical records (0 removed — dataset was clean)
- Flagged 7,754 cancelled shipments (excluded from delay analysis, retained for order-status analysis)
- Standardized region & market naming (fixed casing/whitespace, preserved acronyms like USCA, LATAM, USA)
- **Result:** 100% of records retained after validation

### 2. Delivery Gap Calculation
- Computed `Delay_Gap = Days for shipping (real) − Days for shipment (scheduled)`
- Classified every order as **On-time**, **Delayed**, or **Early**

### 3. Overall Delivery Performance
| Metric | Value |
|---|---|
| On-Time Delivery Rate | **18.70%** |
| Late Delivery Risk Ratio | **54.83%** |
| Average Delivery Delay | **0.57 days** |

### 4. Shipping Mode Efficiency
| Shipping Mode | Late Risk (%) |
|---|---|
| First Class | ~95% |
| Second Class | ~77% |
| Same Day | ~46% |
| Standard Class | ~38% |

**Key insight:** "Premium" shipping modes are actually the least reliable. Standard Class — used in ~60% of orders — is both the most common and most dependable option.

### 5. Regional & Market Diagnostics
- Highest risk: Central Africa, South Asia, East Africa (~56–58%)
- Best performer: Canada (~49%) — a useful internal benchmark

### 6. Customer Segment Impact
- Risk is nearly identical across Consumer, Corporate, and Home Office segments (~54–55%)
- Confirms delay risk is structural (mode/region-driven), not customer-driven — no hidden bias in routing

## 📁 Repo Contents
- `01_Data_Cleaningand validation.ipynb` — Data cleaning & validation
- `02_Delivery_Gap_calculation.ipynb` — Delay gap + classification
- `03_EDA.ipynb` — Exploratory analysis & charts
- `app.py` — Streamlit dashboard (KPIs, filters, interactive charts, regional heatmap)
- `compressed_data.csv.gz` — Cleaned dataset
- `requirements.txt` — Dependencies
- `Research_Paper.docx` — Full methodology, findings, and recommendations
- `Executive_Summary.docx` — 1-page summary for stakeholders

## 🖥️ Dashboard Features
- KPI scorecards (on-time rate, risk ratio, avg delay)
- Filters: Shipping Mode, Market, Order Region, Customer Segment, Date Range
- Delivery performance pie chart & delay distribution histogram
- Shipping mode risk comparison
- Region × Shipping Mode risk heatmap

## 🛠️ Tech Stack
Python · Pandas · NumPy · Plotly · Streamlit · Jupyter Notebook

## ▶️ Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📊 Core Recommendations
- Re-evaluate SLA promises for First Class and Second Class shipping
- Prioritize root-cause investigation in Central Africa, South Asia, and East Africa
- Use Canada's operational model as a best-practice benchmark
- Adopt the live dashboard for ongoing monitoring instead of static reporting

## 📌 Status
Data cleaning, KPI analysis, EDA, and the Streamlit dashboard are complete. Research paper and executive summary are complete and included above. Deployed on Streamlit Community Cloud.


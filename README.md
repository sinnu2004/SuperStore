SuperStore Sales Analysis

End-to-end data analysis project on the global SuperStore retail dataset (2011–2014), covering data cleaning and EDA in Python, pivot-table reporting in Excel, and an interactive dashboard in Power BI.

📌 Project Overview

The project analyzes ~51,000 order-level transactions from a global superstore operating across 7 markets (APAC, EU, US, LATAM, EMEA, Africa, Canada) to uncover sales and profit trends by year, category, region, market, and state — and to surface where the business is losing money despite strong sales (heavy discounting).

🗂️ Repository Structure
SuperStore/
├── SuperStoreAnalysis.py     # Python script: data cleaning + EDA
├── SuperStore.xlsx           # Raw data + pivot tables/charts (Sheet: SuperStoreOrders)
├── SuperStorePivot.xlsx      # Pivot table workbook
└── SuperStore.pbix           # Power BI interactive dashboard
📊 Dataset
Source: SuperStoreOrders.csv (~51,290 rows, 21 columns)
Key fields: order_date, ship_date, ship_mode, customer_name, segment, state, country, market, region, category, sub_category, product_name, sales, quantity, discount, profit, shipping_cost, order_priority, year
Time range: 2011–2014
Grain: one row per order line item
🛠️ Tools & Tech Stack
Layer	Tool	Purpose
Data cleaning & EDA	Python (pandas, numpy, matplotlib, seaborn)	Type casting, summary statistics, exploratory plots
Ad-hoc reporting	Microsoft Excel	Pivot tables, pivot charts, slicers
Interactive dashboard	Power BI	KPI cards, slicers, drill-down visuals
🐍 Python Analysis (SuperStoreAnalysis.py)
Loaded the raw CSV and inspected schema/nulls with .info(), .head(), .tail()
Cleaned the sales column (stripped comma-formatted strings, cast to numeric)
Computed core KPIs: average / max / min sales and profit
Visualized profit by year using a Seaborn bar plot
📈 Excel Pivot Reporting

Dashboard & Images
<img width="937" height="455" alt="image" src="https://github.com/user-attachments/assets/5c7e63b5-658d-48a9-b1e5-aa90e19b6753" />

<img width="802" height="291" alt="image" src="https://github.com/user-attachments/assets/fb4b9c04-09b1-44e2-a4ee-78bae1519972" />


Built using SuperStoreOrders as the source, with pivot tables/charts on separate sheets:

Sales by category × year (pivot table + slicer on year)
Sales pie chart by category (Furniture / Office Supplies / Technology)
Profit by year (column chart, 2011–2014)
Sales by market × year, trended as a line chart
Region-level sales pivot table
📊 Power BI Dashboard — "Super Store Sales"

KPI cards: Sum of Profit (1.47M), Sum of Sales (13M), Max Profit (8.40K), Max Sales (23K)

Slicers: Year (2011–2014), Quarter (Q1–Q4)

Visuals:

Sum of profit by year (column chart) — steady YoY growth, 0.25M → 0.50M
Sum of profit by market (donut chart) — APAC leads at 31.09%, followed by US (26.49%) and EU (20.35%)
Sum of sales by category (pie chart) — Technology 37.53%, Office Supplies 32.52%, Furniture 29.96%
Sum of sales by region (bar chart) — South and North lead within APAC/US markets
Sum of discount by category (bar chart) — Furniture carries the highest discount burden
Sum of profit by state (line chart) — England highest, Île-de-France lowest among top states shown
🔑 Key Insights
Profit grew consistently every year (2011 → 2014), roughly doubling over the period.
APAC is the top profit-generating market (31%), ahead of US and EU.
Technology is the top-selling category, but Furniture attracts the highest discounts, which likely compresses its margins.
Sales are concentrated in a handful of regions (South, North, Oceania) — a small subset of regions drives most of the volume.
Profit varies sharply by state, indicating discounting/logistics costs are not uniform across geographies.
▶️ How to Reproduce
Python EDA
bash
   pip install pandas numpy matplotlib seaborn
   python SuperStoreAnalysis.py
Excel — open SuperStorePivot.xlsx, refresh pivot tables if the source data changes.
Power BI — open SuperStore.pbix in Power BI Desktop, click Refresh to reload data.
👤 Author

Project by Saurabh — built as a self-driven data analytics project to practice the full pipeline: raw data → Python cleaning/EDA → Excel reporting → Power BI dashboarding.

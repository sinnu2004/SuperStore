Superstore Sales Analysis

Exploratory data analysis and dashboarding on the SuperStore retail orders 
dataset, covering sales, profit, and discount patterns across regions, 
markets, categories, and time.

What's in this project
- Python (Pandas, NumPy, Seaborn): data cleaning and summary statistics
- Power BI: interactive dashboard for visual exploration by year, market, 
  category, region, and state

Data Cleaning
- Loaded the raw SuperStoreOrders dataset with Pandas
- Cleaned the sales column (stripped comma separators, coerced to numeric) 
  before analysis
- Computed average, maximum, and minimum for sales and profit using NumPy
- Used Seaborn to plot profit by year as an initial check before building 
  the dashboard

Dashboard Overview
Top-level KPIs: 503.44K total profit, 4M total sales, 8.40K max profit, 
18K max sales.

Visuals include:
- Sum of profit by year (2011–2014) — general upward trend, dip in 2012
- Sum of profit by market (APAC, US, EU, LATAM, Africa) — APAC leads at 32.71%
- Sum of sales by category (Technology, Furniture, Office Supplies) — fairly 
  even split, Office Supplies slightly ahead
- Sum of sales by region — South and North lead, EMEA lowest
- Sum of discount by category, filterable by quarter
- Sum of profit by state — top states include New York, California, England
- Year and quarter filters applied across all visuals

Key Observations
- Profit grew year-over-year overall, 2014 was the strongest year (168K)
- APAC and US together account for over half of total profit by market
- Sales are fairly evenly split across categories, Office Supplies slightly 
  ahead
- South and North lead by sales volume; EMEA lags

Tools Used
- Python: Pandas, NumPy, Matplotlib, Seaborn
- Power BI: dashboard design, DAX-based aggregations, interactive filters

Dashboard Image 
<img width="897" height="486" alt="Screenshot 2026-08-13 120855" src="https://github.com/user-attachments/assets/4177c05b-b7aa-4351-ad66-5e939877a205" />


Note: built on a public-style retail dataset for practice/skill-building 
purposes, not real company data.

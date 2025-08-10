# 🛍 Sales Dashboard Project

## 📌 Project Overview
This project is a **Sales Analytics Dashboard** built using **Power BI**.  
It provides insights into:
- Sales Overview
- Inventory Tracking
- Customer Insights
- Supplier Management
- Returns & Refunds
- Financial Summary

The project also demonstrates **data cleaning** and **transformation** steps using Python & Power BI Power Query.

---

## 📂 Project Structure

```bash
Sales-Dashboard-Project/
│
├── data/
│   ├── sales_overview.csv
│   ├── inventory_tracking.csv
│   ├── customer_insights.csv
│   ├── supplier_management.csv
│   ├── returns_refunds.csv
│   ├── financial_summary.csv
│
├── cleaning_scripts/
│   ├── clean_sales.py
│   ├── clean_inventory.py
│   ├── clean_customers.py
│   ├── clean_suppliers.py
│   ├── clean_returns.py
│   ├── clean_financials.py
│
├── dashboards/
│   ├── Sales_Dashboard.pbix
│
├── README.md
🚀 Features
Interactive Dashboards with filters & slicers

Data Cleaning of inconsistent & dirty data

KPIs Tracking for revenue, profit, inventory status, etc.

Region-wise & Category-wise breakdown

Financial health monitoring

📦 Requirements
🔹 Software Needed
Power BI Desktop

Python 3.9+

Git

🔹 Python Libraries
bash
Copy
Edit
pip install pandas numpy faker
🛠 Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/Amalgamator04/1cr.git
cd sales-dashboard
2️⃣ Prepare Data
We use dirty data generated with faker and clean it before loading to Power BI.

Run the cleaning scripts:

bash
Copy
Edit
python cleaning_scripts/clean_sales.py
python cleaning_scripts/clean_inventory.py
python cleaning_scripts/clean_customers.py
python cleaning_scripts/clean_suppliers.py
python cleaning_scripts/clean_returns.py
python cleaning_scripts/clean_financials.py
Cleaned files will be saved inside:

bash
Copy
Edit
data/cleaned/
📊 Power BI Steps
Open Power BI Desktop

Go to Get Data → CSV and import cleaned files from data/cleaned/

Perform transformations in Power Query if needed

Create 6 pages of dashboards:

Sales Overview

Inventory Tracking

Customer Insights

Supplier Management

Returns & Refunds

Financial Summary

Add filters, slicers, and KPIs

Save the .pbix file in dashboards/

📈 Dashboard Pages
Page Name	Key Visuals
Sales Overview	Revenue trend, top products, region split
Inventory Tracking	Stock levels, restock trends
Customer Insights	Active customers, retention rate
Supplier Management	Top suppliers, supplier performance
Returns & Refunds	Return rate, refund amounts
Financial Summary	Profit, expenses, revenue growth

🧪 Sample Data
The data used in this project is synthetic and generated using Faker.
This allows for realistic but non-sensitive records for practice.

🤝 Contribution
Pull requests are welcome! Please fork the repo and create a new branch for your changes.

📜 License
This project is licensed under the MIT License.

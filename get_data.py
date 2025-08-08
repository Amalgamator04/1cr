from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker()

# 1. Sales Overview Data
sales_data = []
for _ in range(200):
    sales_data.append({
        "Order_ID": fake.uuid4(),
        "Date": fake.date_between(start_date="-1y", end_date="today"),
        "Product": fake.word(),
        "Category": random.choice(["Electronics", "Clothing", "Home", "Beauty", "Sports"]),
        "Quantity": random.randint(1, 10),
        "Price": round(random.uniform(5, 500), 2),
        "Discount": round(random.uniform(0, 0.3), 2),
        "Region": random.choice(["North", "South", "East", "West"])
    })
sales_df = pd.DataFrame(sales_data)

# 2. Customer Insights Data
customers_data = []
for _ in range(150):
    customers_data.append({
        "Customer_ID": fake.uuid4(),
        "Name": fake.name(),
        "Age": random.randint(18, 70),
        "Gender": random.choice(["Male", "Female", "Other"]),
        "Region": random.choice(["North", "South", "East", "West"]),
        "Join_Date": fake.date_between(start_date="-3y", end_date="today"),
        "Total_Spend": round(random.uniform(100, 10000), 2),
        "Loyalty_Score": random.randint(1, 10)
    })
customers_df = pd.DataFrame(customers_data)

# 3. Inventory Management Data
inventory_data = []
for _ in range(100):
    inventory_data.append({
        "Product_ID": fake.uuid4(),
        "Product_Name": fake.word(),
        "Category": random.choice(["Electronics", "Clothing", "Home", "Beauty", "Sports"]),
        "Stock_Level": random.randint(0, 500),
        "Reorder_Level": random.randint(10, 100),
        "Supplier": fake.company(),
        "Last_Updated": fake.date_between(start_date="-6m", end_date="today")
    })
inventory_df = pd.DataFrame(inventory_data)

# 4. Marketing Campaign Performance Data
campaign_data = []
for _ in range(80):
    campaign_data.append({
        "Campaign_ID": fake.uuid4(),
        "Campaign_Name": fake.catch_phrase(),
        "Start_Date": fake.date_between(start_date="-1y", end_date="-1m"),
        "End_Date": fake.date_between(start_date="-1m", end_date="today"),
        "Channel": random.choice(["Email", "Social Media", "TV", "Radio", "Billboard"]),
        "Spend": round(random.uniform(1000, 50000), 2),
        "Revenue": round(random.uniform(2000, 100000), 2),
        "ROI": round(random.uniform(-0.5, 2), 2)
    })
campaign_df = pd.DataFrame(campaign_data)

# 5. Financial Performance Data
finance_data = []
for _ in range(60):
    finance_data.append({
        "Month": fake.date_between(start_date="-2y", end_date="today").strftime("%Y-%m"),
        "Revenue": round(random.uniform(5000, 200000), 2),
        "Cost": round(random.uniform(2000, 150000), 2),
        "Profit": round(random.uniform(-5000, 50000), 2),
        "Tax": round(random.uniform(500, 20000), 2)
    })
finance_df = pd.DataFrame(finance_data)

# 6. Employee Performance Data
employee_data = []
for _ in range(120):
    employee_data.append({
        "Employee_ID": fake.uuid4(),
        "Name": fake.name(),
        "Department": random.choice(["Sales", "Marketing", "HR", "IT", "Finance", "Operations"]),
        "Joining_Date": fake.date_between(start_date="-5y", end_date="today"),
        "Performance_Score": random.randint(1, 10),
        "Projects_Handled": random.randint(0, 20),
        "Salary": round(random.uniform(20000, 150000), 2)
    })
employee_df = pd.DataFrame(employee_data)

# Save to CSV files
sales_df.to_csv("sales_overview.csv", index=False)
customers_df.to_csv("customer_insights.csv", index=False)
inventory_df.to_csv("inventory_management.csv", index=False)
campaign_df.to_csv("marketing_campaign.csv", index=False)
finance_df.to_csv("financial_performance.csv", index=False)
employee_df.to_csv("employee_performance.csv", index=False)


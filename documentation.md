# 📊 Sales & Operations Dashboard - Data Dictionary

This document describes the structure, purpose, and fields for all datasets used across the six dashboard pages.

---

## 1. **Sales Data** (`sales_data.csv`)
**Purpose:**  
Tracks individual sales transactions for analysis of revenue, units sold, and customer purchases.

**Columns:**
- **Order_ID** *(string)* – Unique identifier for each order.
- **Date** *(date)* – Date of the transaction.
- **Customer_ID** *(string)* – Unique identifier for the customer.
- **Product_ID** *(string)* – Unique identifier for the product sold.
- **Product_Category** *(string)* – Category of the product (e.g., Skincare, Makeup, Haircare).
- **Quantity** *(integer)* – Number of units sold in the order.
- **Unit_Price** *(float)* – Price per unit of the product.
- **Total_Amount** *(float)* – Quantity × Unit Price.
- **Payment_Method** *(string)* – Mode of payment (e.g., Credit Card, Cash, UPI).
- **Region** *(string)* – Geographic sales region.
- **Sales_Channel** *(string)* – Online, In-store, or Distributor.

---

## 2. **Inventory Data** (`inventory_data.csv`)
**Purpose:**  
Monitors stock levels and product availability for supply chain and restocking decisions.

**Columns:**
- **Product_ID** *(string)* – Unique product identifier.
- **Product_Name** *(string)* – Name of the product.
- **Category** *(string)* – Product category.
- **Supplier_ID** *(string)* – Unique identifier for supplier.
- **Stock_On_Hand** *(integer)* – Current stock available.
- **Reorder_Level** *(integer)* – Minimum stock before reordering.
- **Reorder_Quantity** *(integer)* – Recommended reorder amount.
- **Last_Restock_Date** *(date)* – Last date stock was replenished.
- **Unit_Cost** *(float)* – Cost price per unit.
- **Warehouse_Location** *(string)* – Storage location.

---

## 3. **Customer Data** (`customer_data.csv`)
**Purpose:**  
Captures customer details for segmentation, marketing, and sales personalization.

**Columns:**
- **Customer_ID** *(string)* – Unique identifier for the customer.
- **Name** *(string)* – Full name.
- **Gender** *(string)* – Male, Female, Other.
- **Age** *(integer)* – Age in years.
- **Email** *(string)* – Customer’s email.
- **Phone** *(string)* – Contact number.
- **Address** *(string)* – Full address.
- **City** *(string)* – City of residence.
- **Region** *(string)* – Region of residence.
- **Join_Date** *(date)* – Date customer first purchased.
- **Preferred_Channel** *(string)* – Online or In-store.

---

## 4. **Marketing Campaign Data** (`marketing_data.csv`)
**Purpose:**  
Records marketing campaigns, target audiences, budgets, and performance metrics.

**Columns:**
- **Campaign_ID** *(string)* – Unique campaign identifier.
- **Campaign_Name** *(string)* – Name of the campaign.
- **Start_Date** *(date)* – Campaign start date.
- **End_Date** *(date)* – Campaign end date.
- **Channel** *(string)* – Marketing medium (e.g., Email, Social Media, TV).
- **Target_Audience** *(string)* – Segment of customers targeted.
- **Budget** *(float)* – Total budget allocated.
- **Spend** *(float)* – Amount spent.
- **Impressions** *(integer)* – Number of views.
- **Clicks** *(integer)* – Clicks generated.
- **Conversions** *(integer)* – Number of sales/leads from campaign.

---

## 5. **Finance Data** (`finance_data.csv`)
**Purpose:**  
Tracks financial transactions for revenue, expenses, and profitability analysis.

**Columns:**
- **Transaction_ID** *(string)* – Unique identifier for financial transaction.
- **Date** *(date)* – Transaction date.
- **Type** *(string)* – Revenue or Expense.
- **Category** *(string)* – Expense category or revenue type.
- **Amount** *(float)* – Transaction amount.
- **Payment_Method** *(string)* – Payment mode used.
- **Department** *(string)* – Department associated (e.g., Sales, Marketing).
- **Description** *(string)* – Transaction details.

---

## 6. **Supplier Data** (`supplier_data.csv`)
**Purpose:**  
Contains information about suppliers for procurement and inventory management.

**Columns:**
- **Supplier_ID** *(string)* – Unique identifier for supplier.
- **Supplier_Name** *(string)* – Supplier’s company or individual name.
- **Contact_Name** *(string)* – Primary contact person.
- **Phone** *(string)* – Contact number.
- **Email** *(string)* – Email address.
- **Address** *(string)* – Supplier address.
- **City** *(string)* – City location.
- **Region** *(string)* – Region location.
- **Country** *(string)* – Country location.
- **Rating** *(integer)* – Supplier rating (1–5).
- **Contract_Start** *(date)* – Contract start date.
- **Contract_End** *(date)* – Contract end date.

---

**Note:**  
These datasets are **synthetic** and generated using Python's `faker` library to mimic realistic business data for practice in **data cleaning, analysis, and dashboard creation**.

#--------------------------------------------------------------------------------#

# 📊 Sales Analytics & Visualization Project

## 🏆 Main Goal
The **primary goal** of this project is to:
1. **Design** dashboards and layouts in **Figma** 🎨.
2. **Clean & analyze** raw sales data using analytics techniques 🧹📈.
3. **Visualize** insights using **Power BI** for interactive decision-making 📊.

---

## 📂 Project Workflow

### 1️⃣ **Figma UI Design**
- Create **dashboard wireframes** and layouts for the Sales Analytics System.
- Focus on **user-friendly design** and clean data presentation.
- **Tools Used**: [Figma](https://www.figma.com)

🖼 **Sample Figma Design Placeholder**  
![Figma Design](path/to/figma_image.png)

---

### 2️⃣ **Data Cleaning & Analytics**
- Use Python (Pandas, NumPy) to clean and preprocess raw sales data.
- Handle:
  - Missing values
  - Outliers
  - Incorrect formats
- Generate summary statistics for better understanding of trends.

🖼 **Data Cleaning Screenshot Placeholder**  
![Data Cleaning](path/to/data_cleaning_image.png)

---

### 3️⃣ **Power BI Dashboard**
- Import cleaned data into Power BI.
- Create **dynamic dashboards** with:
  - KPIs
  - Sales trends
  - Product-wise performance
  - Regional analysis
- Enable interactive filtering for deep-dive analysis.

🖼 **Power BI Dashboard Placeholder**  
![Power BI Dashboard](path/to/powerbi_image.png)

---

## 📊 Features
- **Interactive Sales Trends**
- **Region & Product Category Insights**
- **Profit Margin & KPI Tracking**
- **User-Centric Dashboard Design**


---


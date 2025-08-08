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


Got it — you want **creative** Power BI page ideas based on your datasets, not just generic dashboards.
Here’s a **set of 6+ unique, story-driven Power BI pages** that will make your report look like a professional, interactive data story.

---

## **1️⃣ Overview & KPI Pulse Board**

**Goal:** Give executives a *one-glance* health check.
**Features:**

* Dynamic KPI cards (Total Revenue, Total Orders, Total Customers, Avg. Order Value, YOY Growth %)
* A *trend ribbon* at the top (last 12 months performance sparkline for each KPI)
* Map showing top-performing regions with tooltips
* Clickable slicers (Date Range, Category, Region)
* **Extra flair:** KPI *pulse animation* that blinks if target not met.

---

## **2️⃣ Sales Deep Dive Explorer**

**Goal:** Help sales managers drill down into performance.
**Features:**

* Waterfall chart showing revenue changes by product category
* TreeMap showing top 10 products contribution
* Decomposition Tree (Break sales → Region → Product → Sales Rep)
* Drillthrough to product-level profit margins
* **Extra flair:** Dynamic commentary box generated using DAX (e.g., *"Electronics sales dropped 5% in Q2 due to North region slowdown"*).

---

## **3️⃣ Customer Segmentation & Behavior**

**Goal:** Understand who your customers are & what they buy.
**Features:**

* Age & gender distribution donut charts
* Customer loyalty tier breakdown
* RFM Analysis (Recency, Frequency, Monetary Value) heatmap
* Average order size by customer type
* **Extra flair:** Scatter plot of “Customer Lifetime Value vs Frequency” with clickable customer profiles.

---

## **4️⃣ Supply Chain & Inventory Watchtower**

**Goal:** Keep inventory & supply chain efficient.
**Features:**

* Stock level heatmap by warehouse & product category
* Inventory aging chart (how long products sit before selling)
* Stock-out alerts table (highlighted red)
* Lead time trend chart for suppliers
* **Extra flair:** Gauge visual for “Days of Stock Remaining” with green/yellow/red thresholds.

---

## **5️⃣ Profitability & Cost Breakdown**

**Goal:** See where money is made or lost.
**Features:**

* Profit margin waterfall chart (Revenue → Discounts → COGS → Net Profit)
* Category-wise gross margin % comparison
* Fixed vs Variable costs donut
* ROI analysis for campaigns or products
* **Extra flair:** Small multiples showing “Profit trend” for each product category.

---

## **6️⃣ Forecast & What-If Analysis**

**Goal:** Plan for the future.
**Features:**

* AI/ML forecast visual for next 6–12 months sales
* What-If parameter slider for price change impact
* Seasonal pattern breakdown (sales by month/year)
* **Extra flair:** Scenario selection (Optimistic, Realistic, Pessimistic) with instant KPI recalculation.

---


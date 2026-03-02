# 🛒 Online Retail Description (Transactions)

### 📊 Dataset Overview

This is a transactional data set which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail.The company mainly sells unique all-occasion gifts. Many customers of the company are wholesalers.

Note: It has no missing values

### 📁 Dataset Structure -

The dataset contains 8 columns with the following features:

1. InvoiceNo
   
   Role: ID
   
   Type: Categorical
   
   Description: a 6-digit integral number uniquely assigned to each transaction. If this code starts with letter 'c', it          indicates a cancellation

2. StockCode
 
   Role: ID
   
   Type: Categorical

   Description: a 5-digit integral number uniquely assigned to each distinct product

3. Description
   
   Role: Feature
   
   Type: Categorical
   
   Description: product name		

4. Quantity
   
   Role: Feature
   
   Type: Integer
   
   Description: the quantities of each product (item) per transaction		

5. InvoiceDate
   
   Role: Feature
   
   Type: Date
   
   Description: the day and time when each transaction was generated		

6. UnitPrice
    
   Role: Feature	
   
   Type: Continuous	
   
   Description: product price per unit sterling	

7. CustomerID
    
   Role: Feature

   Type: Categorical	
   
   Description: a 5-digit integral number uniquely assigned to each customer	

8. Country
    
   Role: Feature
	
   Type: Categorical	
   
   Description: the name of the country where each customer resides
   


# 🛒 E-Commerce Customer Behavior and Sales Dataset (Customer)

### 📊 Dataset Overview -

This comprehensive dataset contains 5,000 e-commerce transactions from a Turkish online retail platform, spanning from January 2023 to March 2024. The dataset provides detailed insights into customer demographics, purchasing behavior, product preferences, and engagement metrics.This version simulates multiple orders per customer, making the dataset suitable for RFM segmentation, CLV analysis, and other behavioral clustering studies.

• Each customer now has between 1 and 10 orders spread across time.

• Order_ID values are unique for every transaction (e.g., ORD_1234-1, ORD_1234-2).

• Dates, quantities, discounts, and totals are randomized but statistically consistent with the original distribution.

• Is_Returning_Customer now correctly reflects repeat buyers.

### 🎯 Use Cases -

This dataset is perfect for:

1. Customer Segmentation Analysis: Identify distinct customer groups based on behavior
2. Sales Forecasting: Predict future sales trends and patterns
3. Recommendation Systems: Build product recommendation engines
4. Customer Lifetime Value (CLV) Prediction: Estimate customer value
5. Churn Analysis: Identify customers at risk of leaving
6. Marketing Campaign Optimization: Target customers effectively
7. Price Optimization: Analyze price sensitivity across categories
8. Delivery Performance Analysis: Optimize logistics and shipping

### 📁 Dataset Structure -

The dataset contains 18 columns with the following features:

• Order Information -
Order_ID: Unique identifier for each order (ORD_XXXXXX format)
Date: Transaction date (2023-01-01 to 2024-03-26)

• Customer Demographics:
Customer_ID: Unique customer identifier (CUST_XXXXX format)
Age: Customer age (18-75 years)
Gender: Customer gender (Male, Female, Other)
City: Customer city (10 major Turkish cities)

• Product Information:
Product_Category: 8 categories (Electronics, Fashion, Home & Garden, Sports, Books, Beauty, Toys, Food)
Unit_Price: Price per unit (in TRY/Turkish Lira)
Quantity: Number of units purchased (1-5)

• Transaction Details:
Discount_Amount: Discount applied (if any)
Total_Amount: Final transaction amount after discount
Payment_Method: Payment method used (5 types)

• Customer Behavior Metrics:
Device_Type: Device used for purchase (Mobile, Desktop, Tablet)
Session_Duration_Minutes: Time spent on website (1-120 minutes)
Pages_Viewed: Number of pages viewed during session (1-50)
Is_Returning_Customer: Whether customer has purchased before (True/False)

• Post-Purchase Metrics:
Delivery_Time_Days: Delivery duration (1-30 days)
Customer_Rating: Customer satisfaction rating (1-5 stars)

### 📈 Key Statistics - 

1. Total Records: 5,000 transactions

2. Date Range: January 2023 - March 2024 (15 months)

3. Average Transaction Value: ~450 TRY

4. Customer Satisfaction: 3.9/5.0 average rating

5. Returning Customer Rate: 60%

6. Mobile Usage: 55% of transactions

### 🔍 Data Quality - 

✅ No missing values

✅ Consistent formatting across all fields

✅ Realistic data distributions

✅ Proper data types for all columns

✅ Logical relationships between features

### 💡 Sample Analysis Ideas -

• Customer Segmentation with K-Means Clustering
• Segment customers based on spending, frequency, and recency
• Sales Trend Analysis
• Identify seasonal patterns and peak shopping periods
• Product Category Performance
• Compare revenue, ratings, and return rates across categories
• Device-Based Behavior Analysis
• Understand how device choice affects purchasing patterns
• Predictive Modeling
• Build models to predict customer ratings or purchase amounts
• City-Level Market Analysis
• Compare market performance across different cities

### 🛠️ Technical Details -

File Format: CSV (Comma-Separated Values)

Encoding: UTF-8

File Size: ~500 KB

Delimiter: Comma (,)

### 📚 Column Descriptions - 

Column Name              Data Type         Description                Example

Order_ID                 String            Unique order identifier    ORD_001337

Customer_ID              String            Unique customer identifier CUST_01337

Date                     DateTime          Transaction date           2023-06-15

Age                      Integer           Customer age               35

Gender                   String            Customer gender            Female

City                     String            Customer city              Istanbul

Product_Category         String            Product category           Electronics

Unit_Price               Float             Price per unit             1299.99

Quantity                 Integer           Units purchased            2

Discount_Amount          Float             Discount applied           129.99

Total_Amount             Float             Final amount paid          2469.99 

Payment_Method           String            Payment method             Credit Card 

Device_Type              String            Device used                Mobile

Session_Duration_Minutes Integer           Session time               15

Pages_Viewed             Integer           Pages viewed               8

Is_Returning_Customer    Boolean           Returning customer         True

Delivery_Time_Days       Integer           Delivery duration          3

Customer_Rating          Integer           Satisfaction rating        5



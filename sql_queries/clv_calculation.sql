USE retail;

-- Check date range of data
SELECT MIN(Date), MAX(Date) FROM cust_behaviour;

-- Create past customer features table (2023)
DROP TABLE IF EXISTS customer_features_past;

CREATE TABLE customer_features_past AS
SELECT 
    Customer_ID,
    COUNT(DISTINCT Order_ID) AS num_orders,
    SUM(Total_Amount) AS total_spent,
    AVG(Total_Amount) AS avg_order_value,
    MIN(Date) AS first_purchase,
    MAX(Date) AS last_purchase,
    DATEDIFF(MAX(Date), MIN(Date)) AS customer_age_days,
    DATEDIFF('2023-12-31', MAX(Date)) AS recency_days
FROM cust_behaviour
WHERE Date BETWEEN '2023-01-01' AND '2023-12-31'
GROUP BY Customer_ID;

-- Create future 12-month CLV table (2024 Q1)
DROP TABLE IF EXISTS customer_future_clv;

CREATE TABLE customer_future_clv AS
SELECT 
    Customer_ID,
    SUM(Total_Amount) AS future_12m_clv
FROM cust_behaviour
WHERE Date BETWEEN '2024-01-01' AND '2024-03-25'
GROUP BY Customer_ID;
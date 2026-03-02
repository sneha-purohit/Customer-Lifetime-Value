-- Create database and use it
CREATE DATABASE IF NOT EXISTS retail;
USE retail;

-- Explore existing tables
SHOW DATABASES;
SELECT * FROM cust_behaviour;
SELECT COUNT(*) FROM cust_behaviour;
DESCRIBE cust_behaviour;

-- Create aggregated customer features table
DROP TABLE IF EXISTS customer_features;

CREATE TABLE customer_features AS
SELECT 
    Customer_ID,
    COUNT(DISTINCT Order_ID) AS num_orders,
    SUM(Total_Amount) AS total_spent,
    AVG(Total_Amount) AS avg_order_value,
    MIN(Date) AS first_purchase,
    MAX(Date) AS last_purchase,
    DATEDIFF(MAX(Date), MIN(Date)) AS customer_age_days,
    DATEDIFF(CURDATE(), MAX(Date)) AS recency_days
FROM cust_behaviour
GROUP BY Customer_ID;

-- Check sample data
SELECT * FROM customer_features LIMIT 10;
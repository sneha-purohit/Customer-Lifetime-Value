USE retail;

-- Create RFM segmentation table with NTILE scoring
DROP TABLE IF EXISTS rfm_segmentation;

CREATE TABLE rfm_segmentation AS
SELECT 
    *,
    NTILE(5) OVER (ORDER BY recency_days ASC) AS r_score,
    NTILE(5) OVER (ORDER BY num_orders DESC) AS f_score,
    NTILE(5) OVER (ORDER BY total_spent DESC) AS m_score
FROM customer_features;

-- Create customer segments based on RFM scores
DROP TABLE IF EXISTS customer_segments;

CREATE TABLE customer_segments AS
SELECT 
    *,
    CASE
        WHEN r_score >= 4 AND f_score >= 4 AND m_score >= 4 THEN 'Champions'
        WHEN r_score >= 4 AND f_score >= 3 THEN 'Loyal Customers'
        WHEN r_score >= 4 AND f_score <= 2 THEN 'New Customers'
        WHEN r_score <= 2 AND f_score >= 3 THEN 'At Risk'
        WHEN r_score <= 2 AND f_score <= 2 THEN 'Lost'
        ELSE 'Potential'
    END AS customer_segment
FROM rfm_segmentation;

-- View top 10 segmented customers
SELECT * FROM customer_segments LIMIT 10;
SELECT product_category,
       COUNT(*) AS total_orders,
       ROUND(SUM(total_amount_pkr), 2) AS total_revenue
FROM customer_orders
GROUP BY product_category
ORDER BY total_revenue DESC;
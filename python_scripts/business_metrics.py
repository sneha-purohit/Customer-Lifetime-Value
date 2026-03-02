def marketing_roi(predicted_clv, segment_col, cost_per_vip=50):
    vip_customers = predicted_clv[segment_col == "VIP"]
    budget = len(vip_customers) * cost_per_vip
    expected_revenue = vip_customers.sum()
    roi = (expected_revenue - budget) / budget * 100 if budget > 0 else 0
    return roi, budget, len(vip_customers)
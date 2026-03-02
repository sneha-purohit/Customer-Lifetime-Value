def assign_segment(clv):
    if clv < 500:
        return "Low"
    elif clv < 1500:
        return "Medium"
    elif clv < 5000:
        return "High"
    else:
        return "VIP"
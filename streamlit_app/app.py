# streamlit_app/app.py

import streamlit as st
import pandas as pd
import numpy as np
import pickle
from pathlib import Path

# =============================
# PATHS (robust)
# =============================
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "Data" / "customer_features.csv"
MODEL_PATH = BASE_DIR / "models" / "clv_model.pkl"

# =============================
# LOAD DATA & MODEL
# =============================
@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

@st.cache_resource
def load_model():
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

df = load_data()
model = load_model()


# =============================
# FEATURES (MATCH TRAINING)
# =============================
FEATURES = [
    "num_orders",
    "avg_order_value",
    "order_value_std",
    "recency_days",
    "customer_age_days",
    "months_active",
    "purchase_growth"
]

# Ensure same preprocessing as training
df[FEATURES] = df[FEATURES].fillna(0)

# =============================
# SEGMENT FUNCTION
# =============================
def assign_segment(clv):
    if clv < 500:
        return "Low"
    elif clv < 1500:
        return "Medium"
    elif clv < 5000:
        return "High"
    else:
        return "VIP"

# =============================
# UI
# =============================
st.set_page_config(page_title="Customer CLV Analyzer", layout="wide")

st.title("💰 Customer Lifetime Value Intelligence System")
st.markdown("Predict customer value, segment customers, and drive marketing ROI")

# =============================
# CUSTOMER SELECT
# =============================
customer_id = st.selectbox("Select Customer ID", df["customer_id"].dropna().unique())

customer = df[df["customer_id"] == customer_id].iloc[0]

# =============================
# PREDICT CLV (log → real)
# =============================
X = customer[FEATURES].fillna(0).values.reshape(1, -1)
pred_log = model.predict(X)[0]
predicted_clv = np.expm1(pred_log)

segment = assign_segment(predicted_clv)

# =============================
# METRICS
# =============================
col1, col2, col3 = st.columns(3)

col1.metric("Predicted CLV ($)", f"{predicted_clv:,.0f}")
col2.metric("Customer Segment", segment)
col3.metric("Total Orders", int(customer["num_orders"]))

# =============================
# RECOMMENDATIONS
# =============================
st.subheader("📊 Recommended Business Actions")

if segment == "VIP":
    st.success("🌟 VIP Customer: Offer premium support, loyalty rewards")
elif segment == "High":
    st.info("📈 High Value: Upsell premium products & personalized offers")
elif segment == "Medium":
    st.warning("📊 Medium Value: Increase engagement & cross-sell")
else:
    st.error("⚠️ Low Value / At Risk: Retention campaigns & discounts")

# =============================
# FEATURE IMPORTANCE
# =============================
st.subheader("🔎 Value Drivers")

if hasattr(model, "feature_importances_"):
    importance_df = pd.DataFrame({
        "Feature": FEATURES,
        "Importance": model.feature_importances_
    }).sort_values(by="Importance", ascending=False)

    st.bar_chart(importance_df.set_index("Feature"))

# =============================
# CUSTOMER PROFILE
# =============================
st.subheader("👤 Customer Profile")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Orders", int(customer["num_orders"]))
c2.metric("Avg Order Value", f"{customer['avg_order_value']:.0f}")
c3.metric("Recency (days)", int(customer["recency_days"]))
c4.metric("Months Active", int(customer["months_active"]))

# =============================
# SEGMENT OVERVIEW
# =============================
st.subheader("📊 Customer Segmentation Overview")

df["predicted_clv"] = np.expm1(
    model.predict(df[FEATURES].fillna(0))
)
df["CLV_Segment"] = df["predicted_clv"].apply(assign_segment)

segment_summary = df.groupby("CLV_Segment").agg(
    Customers=("customer_id", "count"),
    Avg_CLV=("predicted_clv", "mean")
).round(2)

st.dataframe(segment_summary)

# =============================
# ROI SIMULATION
# =============================
st.subheader("💵 Marketing ROI Simulation")

vip_customers = df[df["CLV_Segment"] == "VIP"]

marketing_cost_per_customer = st.slider(
    "Marketing Cost per VIP Customer ($)",
    10, 200, 50
)

budget = len(vip_customers) * marketing_cost_per_customer
expected_revenue = vip_customers["predicted_clv"].sum()

roi = (expected_revenue - budget) / budget * 100 if budget > 0 else 0

r1, r2, r3 = st.columns(3)
r1.metric("VIP Customers", len(vip_customers))
r2.metric("Marketing Budget ($)", f"{budget:,.0f}")
r3.metric("Expected ROI (%)", f"{roi:.1f}")

# =============================
# FOOTER
# =============================
st.markdown("---")
st.caption("Customer Lifetime Value Prediction & Segmentation System")
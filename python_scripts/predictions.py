from .feature_engineer import preprocess_features
from .clv_model import predict_clv
from .segmentation import assign_segment

def predict_customer_clv(model, df, features):
    df = preprocess_features(df, features)
    df["predicted_clv"] = predict_clv(model, df[features])
    df["CLV_Segment"] = df["predicted_clv"].apply(assign_segment)
    return df
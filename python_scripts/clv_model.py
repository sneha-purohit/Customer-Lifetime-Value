from sklearn.ensemble import GradientBoostingRegressor
import numpy as np

def train_clv_model(X_train, y_train):
    model = GradientBoostingRegressor(random_state=42)
    model.fit(X_train, y_train)
    return model

def predict_clv(model, X):
    # model was trained on log1p(y)
    preds_log = model.predict(X)
    return np.expm1(preds_log)
import joblib
import pandas as pd
from app.core.config import Settings
from app.cache.redis_cache import set_cached_prediction,get_cached_prediction


model=joblib.load(Settings.MODEL_PATH)


def predict_car_price(data:dict):
    cached_key= " ".join([str(val) for val in data.values])
    cached=get_cached_prediction(cached_key)
    if cached:
        return cached
    input_data=pd.DataFrame([data])
    prediction=model.predict(input_data)[0]
    set_cached_prediction(cached_key,prediction)
    return prediction
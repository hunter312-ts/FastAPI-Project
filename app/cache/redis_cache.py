import json
import redis
from app.core.config import Settings


redis_client=redis.Redis.from_url(Settings.REDIS_URL)

def get_cached_prediction(key:str):
    value=redis_client.get(key)
    if value:
        return json.loads(value)
    return None


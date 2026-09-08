from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.middleware.logging_middleware import LoggingMiddleware
from app.api import routes_auth ,routes_predict
from app.core.exception import register_exception_handler


#title
app=FastAPI(title="Car Price Prediction")

# link the middleware
app.add_middleware(LoggingMiddleware)

#link endpoints
app.include_router(routes_auth.router,tags=['AUTH'])
app.include_router(routes_predict.router ,tags=['Prediction'])

#monitpring using prometheteun
Instrumentator().instrument(app).expose(app)

#add exception Handler
register_exception_handler(app)
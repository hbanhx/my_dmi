from fastapi import FastAPI
from app.api import stations, observations


'''
Purpose: Depends lets you define a callable (function/class) whose result will be passed to your endpoint. You don’t call it directly—FastAPI handles execution and injection.

https://fastapi.tiangolo.com/tutorial/query-params-str-validations/

'''

app = FastAPI(
    title="myDMI", 
    description="Replicate DMI OPEN API with Postgresql", 
    version="1.0",
    )

app.include_router(
    router=stations.router,
    prefix="/myDmi/metObs/collections/station"
)


app.include_router(
    router=observations.router,
    prefix="/myDmi/metObs/collections/observation"
)

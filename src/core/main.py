from fastapi import FastAPI, Query
from src.infrastructure.index.postgress_client import PostgresClient

app = FastAPI()
db = PostgresClient()

@app.get("/search")
def search(q: str = Query(...)):
    results = db.search(q)
    return {"results": results}


@app.get("/")
def read_root():
    return {"message": "DocSeach API is up and Running Successfully"}
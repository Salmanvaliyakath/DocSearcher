from fastapi import FastAPI, Depends, Query
from src.infrastructure.index.postgress_client import PostgresClient
from src.core.schema import ItemQueryParams, SearchResponse


# Create an instance of the FastAPI application
app = FastAPI()

# Initialize the Postgres database client
db = PostgresClient()


def get_query_params(key: str = Query(..., min_length=2, max_length=50)):
    """
    Validates and returns query parameters as a Pydantic model.
    
    """
    return ItemQueryParams(key=key)


@app.get("/search", response_model=SearchResponse)
def search(query: ItemQueryParams = Depends(get_query_params)):
    """
    Search for documents in the database using a keyword.

    Args:
        query (ItemQueryParams): The validated query parameter from the request.

    Returns:
        SearchResponse: A list of matched documents based on the keyword.
    """
    results = db.search(query.key)
    return {"results": results}


@app.get("/")
def read_root():
    """
    Root endpoint to verify that the API is running.
    
    Returns:
        dict: A simple status message.
    """
    return {"message": "DocSeach API is up and Running Successfully"}
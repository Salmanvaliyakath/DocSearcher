from pydantic import BaseModel, Field
from typing import List


class ItemQueryParams(BaseModel):
    # Defines the expected query parameter for searching.
    # 'key' is a required string field
    key: str = Field(..., min_length=2, max_length=50, description="query")


class Document(BaseModel):
    # Represents a document in the search results.
    file_name: str

class SearchResponse(BaseModel):
    # Defines the response model for a search operation.
    # 'results' is a list of Document objects returned from the search.
    results: List[Document]
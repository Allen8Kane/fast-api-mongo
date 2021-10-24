#from typing import Optional
from pydantic import BaseModel, Field


class User(BaseModel):
    name: str = Field(min_length=1, max_length=15)
    salary: int = Field(ge=0, le= 100_000)
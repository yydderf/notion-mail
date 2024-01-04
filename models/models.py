from pydantic import BaseModel
from functools import total_ordering

class Event(BaseModel):
    title: str
    time: str

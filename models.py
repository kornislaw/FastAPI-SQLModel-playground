from datetime import datetime

from sqlmodel import SQLModel, Field
from typing import Optional


class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    price: int
    created_at: datetime = Field(default=datetime.utcnow)

from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import uuid4

from pydantic import BaseModel


class Order(BaseModel):
    id: str
    item_name: str
    table_number: int
    time_to_cook: int

    @classmethod
    def without_id(
        cls,
        item_name: str,
        table_number: int,
        time_to_cook: int,
    ):
        return cls(
            id=str(uuid4()),
            item_name=item_name,
            table_number=table_number,
            time_to_cook=time_to_cook,
        )


class TableOrder(BaseModel):
    id: str
    item_name: str
    time_to_cook: int


class TableOrderReturn(BaseModel):
    orders: List[TableOrder]

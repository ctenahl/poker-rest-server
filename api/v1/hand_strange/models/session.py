from typing import List
from pydantic import BaseModel

from api.v1.hand_strange.models.table import Table
from api.v1.hand_strange.models.hand import Hand

class Session(BaseModel):
    id : int
    table: Table
    hands: List[Hand]
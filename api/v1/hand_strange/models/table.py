from typing import List
from pydantic import BaseModel

from api.v1.hand_strange.models.card import Card

class Table(BaseModel):
    cards: List[Card]
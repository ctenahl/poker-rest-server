from typing import List
from pydantic import BaseModel

from api.v1.hand_strange.models.card import Card

class Hand(BaseModel):
    user_id: int
    cards: List[Card]
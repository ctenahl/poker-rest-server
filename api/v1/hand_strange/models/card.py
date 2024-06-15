from typing import List, Union
from pydantic import BaseModel, validator

class Card(BaseModel):
    suit: str
    value: Union[str, int]

    @validator("suit")
    @classmethod
    def validate_suit(cls, value):
        if value not in ['C', 'D', 'H', 'S']:
            raise ValueError('Card suit is unknown')
        return value
    
    @validator("value")
    @classmethod
    def validate_value(cls, value):
        value = str(value)
        if value not in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
            raise ValueError('Card value is unknown')
        return value
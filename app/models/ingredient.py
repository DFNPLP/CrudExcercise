from typing import Optional

from pydantic import BaseModel
from pydantic.types import UUID4


class Ingredient(BaseModel):
    id: UUID4
    amount: float  # maybe make a way to scale the recipe by multiplying the amount variable?
    measurement_type: Optional[str]  # what unit the ingredient amount is in. it is possible to leave this blank
    title: str

    # todo, write some code here
    #  Add items here to make the model. What makes up an ingredient? A name? An amount? A measurement type?

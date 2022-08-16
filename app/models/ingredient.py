from pydantic import BaseModel
from pydantic.types import UUID4


class Ingredient(BaseModel):
    id: UUID4
    amount: float  # maybe make a way to scale the recipe by multiplying the amount variable?
    measurementType: str  # it should be possible to leave this blank, i.e. 1 ___ lemon vs 1 tsp cumin
    # ^^^^^ maybe a shorter variable name?
    title: str

    # todo, write some code here
    #  Add items here to make the model. What makes up an ingredient? A name? An amount? A measurement type?

from pydantic import BaseModel
from pydantic.types import UUID4


class Ingredient(BaseModel):
    id: UUID4
    # todo, write some code here
    #  Add items here to make the model. What makes up an ingredient? A name? An amount? A measurement type?

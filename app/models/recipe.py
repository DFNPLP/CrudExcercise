import uuid
from pydantic import BaseModel, root_validator
from pydantic.types import UUID4


class Recipe(BaseModel):
    id: UUID4
    name: str
    description: str

    # todo, write some code here
    #  Add items here to make the model. What makes up a recipe? Temperature in the oven as a float?
    #  A list of ingredients?

    @root_validator(pre=True)
    def insert_id_if_none(cls, values):
        if not values.get("id"):
            values["id"] = uuid.uuid4()
        return values

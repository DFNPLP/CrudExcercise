import uuid
from pydantic import BaseModel, root_validator
from pydantic.types import UUID4


class Recipe(BaseModel):
    id: UUID4
    name: str
    recipeYield: str
    description: str
    ingredientList: str

    """
        i'll leave the list at that, but there are other possible items such as:
        actual cooking instructions for how to prepare the dish
        nutritional information
        cooking time and temperature possibly broken up further into prep time, cooking time, total time, 
            and any special times such as rising or marinating
        possible variations or substitutions
        general post recipe notes to complement the description
     """


    # todo, write some code here
    #  Add items here to make the model. What makes up a recipe? Temperature in the oven as a float?
    #  A list of ingredients?

    @root_validator(pre=True)
    def insert_id_if_none(cls, values):
        if not values.get("id"):
            values["id"] = uuid.uuid4()
        return values

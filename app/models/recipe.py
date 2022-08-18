import uuid
from pydantic import BaseModel, root_validator
from pydantic.types import UUID4
# maybe "from ingredient import Ingredient" or is it "from app.models.ingredient import Ingredient"?
# not sure how many folders back I need to go, if any, since the Recipe and Ingredient classes are in the same folder


class Recipe(BaseModel):
    id: UUID4
    name: str
    recipeYield: str
    description: str
    ingredientList: str  # I assume this should be integrated with the ingredient model?

    """
        i'll leave the list at that for now but there are other possible items such as:
        actual cooking instructions for how to prepare the dish
        nutritional information
        cooking time and temperature possibly broken up further into prep time, cooking time, total time, 
            and any special times such as rising or marinating
        possible variations or substitutions
        notes or tips to complement the description
     """

    # todo, write some code here
    #  Add items here to make the model. What makes up a recipe? Temperature in the oven as a float?
    #  A list of ingredients?

    @root_validator(pre=True)
    def insert_id_if_none(cls, values):
        if not values.get("id"):
            values["id"] = uuid.uuid4()
        return values

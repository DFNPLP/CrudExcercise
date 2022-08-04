from typing import List
from fastapi import APIRouter, HTTPException, Depends
from pydantic import UUID4
from tinydb.table import Document
from app.models.recipe import Recipe
from app.persistence.tinydb import get_db_connection, DbConnection

router = APIRouter()


@router.post("/lembas")
async def post_lembas_bread(
        db_connection_instance: DbConnection = Depends(get_db_connection)
):
    """
    This is just a test to sort of show you how a document gets written.
    This function should be removed when you're done. Note: if you call
    this function multiple times, you'll get multiple lembas entries in
    your DB.
    :param db_connection_instance: The object through which to access the
    DB.
    :return: A 200 status code if the recipe was added.
    """
    recipe_model_instantiation: Recipe = Recipe.parse_obj(
        {
            "name": "Lembas Bread",
            "description": "One small bite will fill the stomach of a"
                           " grown man."
        }
    )

    db_connection_instance.get_db().insert(
        Document(
            # exclude the id so the id doesn't get entered twice...
            # just a quirk of tinydb.
            recipe_model_instantiation.dict(exclude={"id"}),
            doc_id=recipe_model_instantiation.id.int
        )
    )

    return recipe_model_instantiation.id


@router.post("/")
async def post_recipe(recipe: Recipe):
    # todo, write some code here
    raise HTTPException(status_code=501, detail="Function not implemented.")


@router.delete("/")
async def delete_recipe(uuid: UUID4):
    # todo, write some code here
    raise HTTPException(status_code=501, detail="Function not implemented.")


@router.get("/")
async def get_recipe(
        record_id: UUID4 = None,
        db_connection_instance: DbConnection = Depends(get_db_connection)
):
    # todo, for a challenge, add pagination! Set the records per page
    #  count to, say, 20 max.
    if not record_id:
        recipes: List[Document] = db_connection_instance.get_db().all()
        docs_as_model = list(
            [
                Recipe.parse_obj(
                    {**{"id": UUID4(int=recipe.doc_id)}, **recipe})
                for recipe in recipes
            ]
        )
        return {"recipes": docs_as_model}
    else:
        # todo, write some code here
        return {"message": "Hello World"}


@router.put("/")
async def put_recipe(recipe: Recipe):
    # todo, write some code here
    raise HTTPException(status_code=501, detail="Function not implemented.")

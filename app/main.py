from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.controllers.recipes import router as recipe_router
from app.persistence.tinydb import DbConnection


def main(app_to_use):
    """
    Main function to get the ball rolling. Python's a bit different,
    this isn't automatically called.
    :param app_to_use: The FastAPI instance to run.
    """
    app_to_use.include_router(
        recipe_router,
        prefix="/recipes"
    )


def custom_openapi(app_to_use):
    """
    Allows some customization of the 'swagger' or docs page.
    :param app_to_use: The FastAPI instance to run.
    :return: The openapi_schema to be used for the docs page.
    """
    if app_to_use.openapi_schema:
        return app_to_use.openapi_schema
    openapi_schema = get_openapi(
        title="Recipes",
        version="0.0.1",
        description="This is an OpenAPI page! It can serve as documentation.",
        routes=app_to_use.routes,
    )
    #openapi_schema["info"]["x-logo"] = {
    #    "url": "<inset image url here if you want to have a custom logo>"
    #}
    app_to_use.openapi_schema = openapi_schema
    return app_to_use.openapi_schema

# initialize tiny db connection
DbConnection.get_instance()
# get the FastAPI instance
app = FastAPI()
# customize the docs page
app.openapi = lambda: custom_openapi(app)
# start the app
main(app)


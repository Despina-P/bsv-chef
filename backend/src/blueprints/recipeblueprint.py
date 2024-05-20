from flask import Blueprint, jsonify, abort, request
from flask_cors import cross_origin

from src.controllers.recipecontroller import RecipeController
from src.util.dao import getDao
controller = RecipeController(items_dao=getDao(collection_name='item'))

from src.static.diets import Diet, from_string

# instantiate the flask blueprint
recipe_blueprint = Blueprint('recipe_blueprint', __name__)

@recipe_blueprint.route('/', methods=['GET'])
@cross_origin()
def create():
    """Generate a recipe proposal that makes use of the current pantry items but complies to dietary preferences.

    parameters (need to be added to the body of the request):
      diet -- dietary restrictions, either "normal", "vegetarian", or "vegan"
      usage_mode -- usage mode of pantry items, either "optimal" or "random"

    returns: 
      recipe -- A recipe proposal that complies to the given dietary restrictions and optionally makes best use of the existing pantry items (if usage_mode=="optimal")
    """
    try:
        data = request.form.to_dict(flat=False)

        # convert all non-array fields back to simple values
        for key in data:
            if isinstance(data[key], list):
                data[key] = data[key][0]

        diet: Diet = from_string(data['diet'])
        take_best: bool =  (data['usage_mode'] == 'optimal')

        recipe_name: str = controller.get_recipe(diet=diet, take_best=take_best)
        recipe: dict = controller.get_recipe_by_name(name=recipe_name)

        if recipe == None:
            return jsonify({'recipe': 'No recipe found for this configuration'}), 404
        return jsonify({'recipe': recipe}), 200
    
    except Exception as e:
        print(f'{e.__class__.__name__}: {e}')
        abort(500, 'Unknown server error')
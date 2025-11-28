from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["recipe_db"]
recipes_collection = db["recipes"]

def add_recipe(recipe):
    recipes_collection.insert_one(recipe)

def get_recipes():
    return list(recipes_collection.find({}, {"_id": 0}))

# This is a recipe manager
print("Welcome to the recipe manager!")
print("------------------------------")
class Recipe:
    def __init__(self, name, ingredients, steps, preptime, difficulty):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        self.preptime = preptime
        self.difficulty = difficulty
import json
import os
recipes = []
if os.path.exists("recipe.json"):
    with open("recipe.json") as f:
        recipes = json.load(f)
while True:
    operation = str(input("Please choose operation (add recipe, search by name, filter by difficulty, delete a recipe or exit): "))
    if operation == "add recipe":
        ingredients = []
        quant = []
        name = str(input("Enter recipe name: "))
        while True:
            item = str(input("Enter an ingredient (or 'exit' to exit): "))
            if item == "done":
                break
            quantity = str(input("Enter the ingredient's quantity: "))
            ingredients.append(item)
            quant.append(quantity)
        steps = str(input("Please enter specific steps (use comma to seperate): "))
        preptime = str(input("Enter prep time: "))
        difficulty = str(input("Enter a difficulty (easy/medium/hard): "))
        r = Recipe(name, ingredients, steps, preptime, difficulty)
        recipes.append({
            "name": r.name,
            "ingredients": r.ingredients,
            "steps": r.steps,
            "preptime": r.preptime,
            "difficulty": r.difficulty
        })
        with open("recipe.json", "w") as f:
            json.dump(recipes, f)
        print("Recipe added!")
    elif operation == "search by name":
        name = str(input("Enter recipe name: "))
        found = False
        for recipe in recipes:
            if (recipe["name"]) == name:
                found = True
                print(f"Recipe: {recipe['name']}:")
                ingredient_list = []
                for i in range(len(ingredients)):
                    ingredient_list.append({"item": ingredients[i], "quantity": quant[i]})
                print(f"Steps: {recipe['steps']}")
                print(f"Prep time: {recipe['preptime']}")
                print(f"Difficulty: {recipe['difficulty']}")
                with open("recipe.json" , 'w') as f:
                    json.dump(ingredient_list, f)
        if not found:
            print("Recipe not found. Try again.")
    elif operation == "filter by difficulty":
        difficulty = str(input("Choose the difficulty (easy/medium/hard): "))
        for recipe in recipes:
            if (recipe["difficulty"]) == difficulty:
                print(f"{recipe['name']} - {recipe['difficulty']}")
            else:
                print("No recipe found!")
    elif operation == "delete a recipe":
        name = str(input("Enter recipe name: "))
        for recipe in recipes:
            if (recipe["name"]) == name:
                recipes.remove(recipe)
                break
            print("Recipe removed.")
            with open("recipe.json", "w") as f:
                json.dump(recipes, f)
    elif operation == "exit":
        break
    else:
        print("Invalid operation. Try again")
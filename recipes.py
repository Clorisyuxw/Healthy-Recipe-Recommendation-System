# 定义食谱数据库
recipes_db = [
    {
        "name": "Fish-Flavored Eggplant",
        "ingredients": ["Eggplant", "ground pork", "garlic", "ginger", "doubanjiang (fermented bean paste)"],
        "instructions": "1. Cut the eggplant into strips and deep fry until golden."
                        "\n2. Stir fry minced garlic, ginger, and doubanjiang."
                        "\n3. Add ground pork until cooked, then mix in the fried eggplant and stir until evenly coated.",
        "calories": 250,
        "nutrition": {
            "protein": 15,
            "carbs": 30,
            "vitamins": "Vitamin C, Iron"
        },
        "image": "picture/fish_flavored_eggplant.jpg"
    },
    {
        "name": "Stir-Fried Tofu with Vegetables",
        "ingredients": ["tofu", "bell pepper", "carrot", "soy sauce", "ginger", "garlic", "vegetable oil"],
        "instructions": "1. Cut tofu into cubes and fry until golden."
                        "\n2. Remove and set aside. Stir-fry chopped bell peppers and carrots until tender."
                        "\n3. Add minced ginger and garlic. Return tofu to the pan, add soy sauce, and stir well to combine.",
        "calories": 200,
        "nutrition": {
            "protein": 12,
            "carbs": 20,
            "vitamins": "Vitamin A, Vitamin C"
        },
        "image": "picture/stir_fried_tofu.jpg"
    },
    {
        "name": "Cucumber Salad",
        "ingredients": ["cucumber", "garlic", "sesame oil", "vinegar", "sugar", "salt", "chili oil"],
        "instructions": "1. Peel and slice cucumber. Mix with salt and set aside for 10 minutes."
                        "\n2. Squeeze out excess water."
                        "\n3. Combine with minced garlic, sesame oil, vinegar, sugar, and chili oil to taste. Chill before serving.",
        "calories": 120,
        "nutrition": {
            "protein": 2,
            "carbs": 15,
            "vitamins": "Vitamin K, Vitamin C"
        },
        "image": "picture/cucumber_salad.jpg"
    },
    {
        "name": "Kung Pao Chicken",
        "ingredients": ["Chicken breast", "peanuts", "dried chili peppers"],
        "instructions": "1. Cut the chicken into cubes and stir fry until golden."
                        "\n2. Add peanuts and dried chili peppers and stir well."
                        "\n3. Pour in the pre-mixed sauce (soy sauce, vinegar, sugar) and stir until thickened.",
        "calories": 300,
        "nutrition": {
            "protein": 26,
            "carbs": 15,
            "vitamins": "Vitamin B6, Niacin"
        },
        "image": "picture/kung_pao_chicken.jpg"
    },
    {
        "name": "Braised Pork Belly",
        "ingredients": ["Pork belly", "ginger", "garlic"],
        "instructions": "1. Slice the pork belly and sear until both sides are browned."
                        "\n2. Add ginger and garlic to the pot and stir."
                        "\n3. Pour in dark soy sauce, light soy sauce, sugar, and water. Simmer until the pork is tender.",
        "calories": 600,
        "nutrition": {
            "protein": 35,
            "carbs": 5,
            "vitamins": "Vitamin B1, B12"
        },
        "image": "picture/braised_pork_belly.jpg"
    },
    {
        "name": "Oyster Sauce Lettuce",
        "ingredients": ["Lettuce", "oyster sauce"],
        "instructions": "1. Wash and cut the lettuce into large pieces."
                        "\n2. Blanch the lettuce in boiling water for 30 seconds, then drain."
                        "\n3. Heat oyster sauce in a pan and toss the lettuce to coat.",
        "calories": 80,
        "nutrition": {
            "protein": 2,
            "carbs": 10,
            "vitamins": "Vitamin A, Vitamin C"
        },
        "image": "picture/oyster_sauce_lettuce.jpg"
    }
]

def get_known_ingredients():
    ingredients_set = set()
    for recipe in recipes_db:
        for ingredient in recipe['ingredients']:
            ingredients_set.add(ingredient.strip().lower())
    return list(ingredients_set)

def get_recipes_by_ingredients(user_ingredients):
    matching_recipes = []
    for recipe in recipes_db:
        if all(ingredient.lower() in [ri.lower() for ri in recipe['ingredients']] for ingredient in user_ingredients):
            matching_recipes.append(recipe)
    return matching_recipes

def clean_ingredients(dish_name, dish_ingredients):

    return (dish_name, set(dish_ingredients))


from sets_categories_data import ALCOHOLS

def check_drinks(drink_name, drink_ingredients):

    if any(ingredient in ALCOHOLS for ingredient in drink_ingredients):
        return f"{drink_name} Cocktail"
    else:
        return f"{drink_name} Mocktail"

"""
Planner.py

Generates a weekly meal plan, builds a grocery list,
and estimates cost with a two-step model:

1. Base price by food type  (spice / veg / protein / other)
2. Multiplier by store tier (Walmart, Trader Joe’s, Whole Foods, Aldi, Costco)
"""

#Importing the needed modules
from Meals_API import search_meals_cat, meal_details
import random

#Rough base price per food item (USD)
Base_Price = {
    "spice": 3.0,
    "veg": 7.0,
    "protein": 15.0,
    "other": 5.0
}

#Store price multipliers
Store_Mult = {
    "walmart": 3.0,
    "trader joe's": 1.0,
    "whole foods": 2.0,
    "aldi": 1.6,
    "costco": 2.5,
    "default": 1.5
}

#Keywords to label ingredients
Spice_Keywords = {"salt", "pepper", "garlic", "spice", "powder", "herb"}
Protein_Keywords = {"chicken", "beef", "pork", "tofu", "salmon", "fish", "egg", "turkey", "shrimp"}
Veg_Keywords = {"lettuce", "tomato", "onion", "broccoli", "carrot", "pepper", "spinach", "zucchini", "potato"}

#Modifiers
Modifiers = {"chopped", "minced", "fresh", "raw", "sliced", "diced", "cubed", "whole", "ground", "grated", "clove"}

#Normalize the ingredients
def normalize_ingredients(name: str):
    """
    Lower-case a raw ingredient string and remove descriptive modifiers.

    Examples:
     normalize_ingredients("Chopped Tomatoes")
    'tomato'
    """

    words = name.lower().split()
    core = " ".join(word for word in words if word not in Modifiers)
    #This should treat plurals like singulars. Checks for varying spellings
    if core.endswith(("oes", "xes", "ses", "zes", "ches", "shes")):
        core = core[:-2]            # removes 'es'
    elif core.endswith("ies"):
        core = core[:-3] + "y"      # berries  will now be berry
    elif core.endswith("ves"):
        core = core[:-3] + "f"      #leaves will not be leaf
    elif core.endswith("s") and not core.endswith("ss"):
        core = core[:-1]
    
    return core

#Classifying the ingredients
def classify_ingredients(item:str):
    """
    Categorizing items based on simple keywords
    """
    
    name = item.lower()
    if any(k in name for k in Spice_Keywords):
        return "spice"
    if any(k in name for k in Protein_Keywords):
        return "protein"
    if any(k in name for k in Veg_Keywords):
        return "veg"
    return "other"


#Estimate cost
def estimate_cost(missing_items:list, store:str):
    """
    Estimates grocery cost for missing_items at store.

    Parameters:
    missing_items : list[str]
        Unique, normalised ingredient names.
    store : str
        Store name; affects multiplier.

    Returns:
    float
        Dollar estimate rounded to 2 decimal places.
    """
    
    store_key = store.lower().strip()
    multiplier = Store_Mult.get(store_key, Store_Mult["default"]) #Default mid-range

    #Calculating the cost
    subtotal = 0.0
    for item in missing_items:
        food_type = classify_ingredients(item)
        subtotal +=Base_Price[food_type]
    return subtotal * multiplier


#function to generate a grocery list. Making walmart the default if no argument passes
def meal_planner(category, available_ingredients, meals_per_day, days, store_choice='walmart', budget=None):
    """
    Creates a multi-day meal plan and grocery list.

    Parameters:
    category : str
        Dietary category for recipe search (e.g., "Vegetarian").
    available_ingredients : list[str]
        Items the user already has; will not appear in grocery list.
    meals_per_day : int
        How many different meals to plan per day.
    days : int
        Number of days to plan.
    store_choice : str, default 'walmart'
        Store used for price multiplier.
    budget : float | None
        If supplied, prints a warning when estimate exceeds budget.

    Returns:
    tuple(dict, list[str], float)
        ( meal_plan, grocery_list, total_cost )
        meal_plan : {'Day 1': [mealA, mealB], ...}
        grocery_list : sorted, unique list of ingredients to buy
        total_cost : estimated cost in USD
    """
    
    #Calling the search_meals function
    meals = search_meals_cat(category)
    if not meals:
        raise Exception("No meals found for this category.")
    
    plan = {}
    grocery_list = set()
    total_cost = 0.0

    # Normalise the pantry once for fast look-ups
    owned = {normalize_ingredients(item) for item in available_ingredients}
    #Using a for loop to loop through the days and meals
    for day in range(1, days +1):
        daily_meals = random.sample(meals, meals_per_day)
        meal_names = []

        for meal in daily_meals:
            meal_detail = meal_details(meal['idMeal'])
            if not meal_detail:
                continue

            meal_name = meal_detail['strMeal']
            meal_names.append(meal_name)

            #This checks for ingredients that are missing from available ingredients
            #Loops through 20 possible ingredients
            for i in range(1, 21):
                ing = meal_detail.get(f"strIngredient{i}")
                if not ing or not ing.strip():
                    continue
                
                #Makes sure that the user doesn't have the ingredients
                norm_ing = normalize_ingredients(ing)
                if norm_ing not in owned:
                    grocery_list.add(norm_ing)
        plan[f"Day {day}"] = meal_names
    
    #Estimating the cost with the new system
    total_cost = estimate_cost(sorted(grocery_list), store_choice)

    if budget and total_cost > budget:
        print(f"Warning: Estimated cost (${total_cost:.2f}) exceeds your budget (${budget:.2f}).")

    return plan, sorted(grocery_list), total_cost
    
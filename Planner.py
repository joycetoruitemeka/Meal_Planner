from Meals_API import search_meals, search_meals_cat, meal_details
import random

#Rough base price per food item (USD)
Base_Price = {
    "spice": 5.0,
    "veg": 7.0,
    "protein": 15.0,
    "other": 10.0
}

#Store price multipliers
Store_Mult = {
    "walmart": 3.0,
    "trader joe's": 1.5,
    "whole foods": 2.0,
    "aldi": 2.0,
    "costco": 2.5,
    "other": 3.0
}

#Keywords to label ingredients
Spice_Keywords = {"salt", "pepper", "garlic", "spice", "powder", "herb"}
Protein_Keywords = {"chicken", "beef", "pork", "tofu", "salmon", "fish", "egg", "turkey", "shrimp"}
Veg_Keywords = {"lettuce", "tomato", "onion", "broccoli", "carrot", "pepper", "spinach", "zucchini", "potato"}

#Classifying the ingredients
def classify_ingredients(item:str) -> str:

    name = item.lower()
    if any(k in name for k in Spice_Keywords):
        return "spice"
    if any(k in name for k in Protein_Keywords):
        return "protein"
    if any(k in name for k in Veg_Keywords):
        return "veg"
    return "other"


#Estimate cost
def estimate_cost(missing_items:list, store:str) -> float:
    
    store_key = store.lower().strip()
    multiplier = Store_Mult.get(store_key,) #Default mid-range

    subtotal = 0.0
    for item in missing_items:
        food_type = classify_ingredients(item)
        subtotal +=Base_Price[food_type]
    return subtotal * multiplier


#function to generate a grocery list
def meal_planner(category, available_ingredients, meals_per_day, days, store_choice="walmart", budget=None):
    meals = search_meals_cat(category)
    if not meals:
        raise Exception("No meals found for this category.")
    
    plan = {}
    grocery_list = set()
    total_cost = 0.0

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
            for i in range(1, 21):
                ing = meal_detail.get(f"strIngredient{i}")
                if ing and ing.strip() and ing.lower() not in [x.strip().lower for x in available_ingredients]:
                    grocery_list.add(ing.strip())
        plan[f"Day {day}"] = meal_names
    
    #Estimating the cost with the new system
    total_cost = estimate_cost(sorted(grocery_list), store_choice)

    if budget and total_cost > budget:
        print(f"Warning: Estimated cost (${total_cost:.2f}) exceeds your budget (${budget:.2f}).")

    return plan, sorted(grocery_list), total_cost
    
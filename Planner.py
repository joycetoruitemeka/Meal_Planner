from Meals_API import search_meals, meal_details
import random

#First function to generate a grocery list
def meal_planner(category, available_ingredients, meals_per_day, days, budget=None):
    meals = search_meals(category)
    if not meals:
        raise Exception("No meals found for this category.")
    
    plan = {}
    grocery_list = set()
    total_cost = 0.0
    all_meal_names = []

    for day in range(1, days +1):
        daily_meals = random.sample(meals, meals_per_day)
        meal_names = []

        for meal in daily_meals:
            meal_detail = meal_details(meal['idMeal'])
            meal_name = meal_detail['strMeal']
            meal_names.append(meal_name)

            for i in range(1, 21):
                ing = meal_detail.get(f"strIngredient{i}")
                if ing and ing.strip() and ing.lower() not in avalaible_ingredients:
                    grocery_list.add(ing.strip())
        plan[f"Day {day}"] = meal_names
    
    estimated_price_per_item = 2.5
    total_cost = len(grocery_list) * estimated_price_per_item
    if budget and total_cost > budget:
        print(f"Warning: Estimated cost (${total_cost:.2f}) exceeds your budget (${budget:.2f}).")

    return plan, sorted(list(grocery_list)), total_cost
    
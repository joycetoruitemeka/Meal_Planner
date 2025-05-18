"""
Meals_API.py
-------------
Handles all HTTP requests to TheMealDB.
"""

import requests

#Base URL  for the free developer key 1
Base_URL = "https://www.themealdb.com/api/json/v1/1/"

#Creating a function to search meals by ingredients
def search_meals(ingredient):
    """
    Return a list of meal summaries that include ingredient.

    Parameters:
    ingredient : str
        Single ingredient to search for (e.g., "chicken").

    Returns:
    list[dict]
        List of meals (each dict has idMeal / strMeal / strMealThumb)
        or an empty list if none found or on error.
    """
    try:
        response = requests.get(f"{Base_URL}filter.php?i={ingredient}")
        response.raise_for_status()
        #Parses the JSON into a python dict
        data = response.json()
        return data["meals"] if data ["meals"] else []
    except Exception as e:
        print("Error fetching meals by ingredients:", e)
        return[]

#Search meals by category
def search_meals_cat(category):
    """
    Returns a list of meal summaries in the given category.

    Parameters:
    category : str
        e.g., "Vegetarian", "Seafood", "Vegan".

    Returns:
    list[dict]
        List of meals or empty list. 
    """
    try:
        response = requests.get(f"{Base_URL}filter.php?c={category}")
        response.raise_for_status()
        data = response.json()
        return data["meals"] if data ["meals"] else []
    except Exception as e:
        print("Error fetching meals by category:", e)
        return[]

#Fetch the meal details
def meal_details(meal_id):
    """
    Returns full details for a single meal.

    Parameters:
    meal_id : str | int
        ID returned in 'idMeal'.

    Returns:
    dict | None
        Meal details (20 ingredients etc.) or None on error.
    """
    try:
        response = requests.get(f"{Base_URL}lookup.php?i={meal_id}")
        response.raise_for_status()
        return response.json()["meals"][0]
    except Exception as e:
        print("Error fetching meal details:", e)
        return None
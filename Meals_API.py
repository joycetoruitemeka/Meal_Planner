import requests

Base_URL = "https://www.themealdb.com/api/json/v1/1/"

#Creating a function to search meals by ingredients
def search_meals(ingredient):
    try:
        response = requests.get(f"{Base_URL}filter.php?i={ingredient}")
        response.raise_for_status()
        data = response.json()
        return data["meals"] if data ["meals"] else []
    except Exception as e:
        print("Error fetching meals by ingredients:", e)
        return[]

#Search meals by category
def search_meals_cat(category):
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
    try:
        response = requests.get(f"{Base_URL}lookup.php?i={meal_id}")
        response.raise_for_status()
        return response.json()["meals"][0]
    except Exception as e:
        print("Error fetching meal details:", e)
        return None
from Planner import meal_planner
from Storage import save_to_file

#Making the main function
def main():
    try:
        dietary_pref = input("Enter your dietary preference (e.g., Vegetarian, Seafood, etc.): ").strip()
        available_ingredients = input("Enter available ingredients (comma-spearated): ").lower().split(',')
        available_ingredients = [i.strip() for i in available_ingredients]

        meals_per_day = int(input("Enter number of meals per day: "))
        days = int(input("Enter number of days to plan for: "))
        store_choice = input("Enter the store: ")
        budget = input("Enter budget in dollars (or leave blank): ").strip()
        budget = float(budget) if budget else None

        meal_plan, grocery_list, total_cost = meal_planner(dietary_pref, available_ingredients, meals_per_day, days, store_choice, budget)

        save_to_file("meal_plan.txt", meal_plan)
        save_to_file("grocery_list.txt", grocery_list)

        print("\nMeal Plan:")
        for day, meals in meal_plan.items():
            print(f"{day}: {', '.join(meals)}")

        print("\nGrocery List:")
        for item in grocery_list:
            print(f"- {item}")

        print(f"\nEstimated Total Cost: ${total_cost:.2f}")

    except ValueError:
        print("Invalid input! Please enter numeric values for meals per day, days, and budget.")
    except Exception as e:
        print(f"Something went wrong: {e}")


if __name__== "__main__":
    main()
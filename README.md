🥗 Meal Planner App
A command-line application that helps users plan meals based on dietary preferences, ingredients they already have, and budget constraints. It connects to TheMealDB API to fetch real recipes, generates a grocery list, and estimates costs based on different store types.

📌 Features
🍽 Generate meal plans by dietary preference (Vegetarian, Vegan, Seafood, etc.)

🧾 Auto-generate a grocery list excluding ingredients you already have

💸 Estimate grocery costs based on selected stores (Walmart, Trader Joe's, Whole Foods, Aldi, Costco)

🧠 Intelligent ingredient normalization and classification

✅ Built-in unit tests to validate app functionality

🚀 How It Works
User inputs: 

Dietary preference

Available ingredients

Meals per day and number of days

Preferred grocery store and optional budget

App fetches meals from TheMealDB API and selects random recipes

Filters out ingredients you already own

Classifies missing items and estimates cost

Saves the meal plan and grocery list as .txt files

🧰 Technologies Used
Python 3

TheMealDB API

requests, random, unittest


📂 File Structure
Meal-Planner/
main.py              # Entry point for user interaction
Meals_API.py         # Handles API calls to TheMealDB
Planner.py           # Core logic: planning, cost estimation
Storage.py           # File save utility for plans/lists
tests.py             # Unit tests using unittest
meal_plan.txt        # Generated meal plan (after run)
grocery_list.txt     # Generated shopping list (after run)
README.md            # Project documentation

🛠 Setup & Usage
✅ Requirements
Python 3.8+

Internet connection (for API calls)

▶️ Running the App
git clone https://github.com/joycetoruitemeka/meal-planner-app.git
cd meal-planner-app
python main.py

🧪 Run Tests
python tests.py

📊 Example Output
Meal Plan:
Day 1: Lentil Soup, Vegetable Stir Fry
Day 2: Vegan Chili, Tofu Salad

Grocery List:
- tofu
- bell pepper
- lentil
- chili powder

Estimated Total Cost: $35.80

.

💡 Future Improvements
Add user accounts for saved plans

GUI or web dashboard

Export to PDF or spreadsheet

Advanced budget breakdown


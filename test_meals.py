import unittest
from Planner import meal_planner

class TestMealPlanner(unittest.TestCase):

    def test_meal_plan_structure(self):
        plan, grocery_list, cost = meal_planner("Vegetarian", ["onion", "salt"], 1, 1)
        self.assertIsInstance(plan, dict)
        self.assertGreaterEqual(len(plan), 1)
        self.assertIsInstance(grocery_list, list)
        self.assertIsInstance(cost, float)

    def test_invalid_category(self):
        with self.assertRaises(Exception):
            meal_planner("NonexisttentCategory", [], 1, 1)


if __name__ == "__main__":
    unittest.main()
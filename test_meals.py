"""
tests.py

Light unit tests for the Meal-Planner project.
Ensures planner utilities and main workflow behave as expected.
"""

import unittest
from Planner import meal_planner, normalize_ingredients, classify_ingredients, estimate_cost

class TestMealPlanner(unittest.TestCase):
    """
    Collection of unit tests covering the public helper functions and
    top-level behaviour of the Meal-Planner system.

    """

    def test_meal_plan_structure(self):
        """
        Verifies that the function returns a dict-shaped plan, a list for
        the grocery output, and a float cost estimate when called with
        minimal valid input.
        """
        plan, grocery_list, cost = meal_planner("Vegetarian", ["onion", "salt"], 1, 1)
        self.assertIsInstance(plan, dict)
        self.assertGreaterEqual(len(plan), 1)
        self.assertIsInstance(grocery_list, list)
        self.assertIsInstance(cost, float)

    
    def test_estimated_cost_positive(self):
        """
        Ensures total cost is a positive number and that the helper
        function 'Planner.estimate_cost' produces an identical figure (within
        two decimal places) to the value returned by function 'Planner.meal_planner'.
        """
        _, grocery, cost = meal_planner("Vegetarian", [], 1, 1)
        self.assertGreater(cost, 0.0)
        self.assertAlmostEqual(cost, estimate_cost(grocery, "walmart"), places=2)


    def test_normalize_ingredients(self):
        """
        Confirms that descriptive modifiers are stripped and case is normalised.
        """
        self.assertEqual(normalize_ingredients("Chopped Tomatoes"), "tomato")
        self.assertEqual(normalize_ingredients("FRESH Basil Leaves"), "basil leaf")


    def test_classify_ingredients(self):
        """
        Checks keyword-based food-type classification across all four
        categories: spice, protein, veg, and other.
        """
        self.assertEqual(classify_ingredients("ground black Pepper"), "spice")
        self.assertEqual(classify_ingredients("tofu cubes"), "protein")
        self.assertEqual(classify_ingredients("zucchini"), "veg")
        self.assertEqual(classify_ingredients("lasagna sheets"), "other")


    def test_invalid_category(self):
        """
        Passing a nonexistent dietary category should raise a generic
        Exception as defined inside function 'Planner.meal_planner'.
        """
        with self.assertRaises(Exception):
            meal_planner("NonexisttentCategory", [], 1, 1)


if __name__ == "__main__":
    unittest.main()
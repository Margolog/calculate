import unittest
from calculate import calculate_bonus


class TestCalculateBonus(unittest.TestCase):

    def test_more_than_3_years_with_sick_leave(self):
        result = calculate_bonus(4, True, 100000)
        self.assertAlmostEqual(result, 30000, delta=0.01)

    def test_1_5_to_3_years_with_sick_leave(self):
        result = calculate_bonus(2, True, 80000)
        self.assertAlmostEqual(result, 20000, delta=0.01)

    def test_90_days_to_1_5_years_with_sick_leave(self):
        result = calculate_bonus(1, True, 60000)
        self.assertAlmostEqual(result, 9000, delta=0.01)

    def test_less_than_90_days_with_sick_leave(self):
        result = calculate_bonus(0.5, True, 40000)
        self.assertAlmostEqual(result, 0, delta=0.01)

    def test_more_than_3_years_without_sick_leave(self):
        result = calculate_bonus(5, False, 120000)
        self.assertAlmostEqual(result, 36000, delta=0.01)

    def test_1_5_to_3_years_without_sick_leave(self):
        result = calculate_bonus(2, False, 90000)
        self.assertAlmostEqual(result, 22500, delta=0.01)

    def test_90_days_to_1_5_years_without_sick_leave(self):
        result = calculate_bonus(1, False, 70000)
        self.assertAlmostEqual(result, 10500, delta=0.01)

    def test_less_than_90_days_without_sick_leave(self):
        result = calculate_bonus(0.5, False, 45000)
        self.assertAlmostEqual(result, 0, delta=0.01)


if __name__ == '__main__':
    unittest.main()

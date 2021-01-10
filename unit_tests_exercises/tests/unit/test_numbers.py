import unittest
from unit_tests_exercises.numbers import Numbers


class TestNumbers(unittest.TestCase):
    def test_validate_if_number_is_unit(self):
        """"
        Using method is_unit, it will be sent the number 9;
        """
        numbers = Numbers()
        is_unit = numbers.is_unit(9)
        """
        As the number is unit, it should returns true.
        """
        self.assertEqual(is_unit, True)

    def test_validate_if_number_is_not_unit(self):
        """
        Using method is_unit, it will be sent the number 10;
        """
        numbers = Numbers()
        is_unit = numbers.is_unit(10)
        """
        As the number is unit, it should returns true.
        """
        self.assertEqual(is_unit, False)


if __name__ == '__main__':
    unittest.main()

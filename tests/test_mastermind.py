import unittest
from functions import mastermind


class MastermindTestCase(unittest.TestCase):

    def setUp(self):
        self.key_list = [5, 5, 1, 2]
        self.correct_guess = [5, 5, 1, 2]
        self.incorrect_guess = [5, 1, 2, 5]
        self.two_matches = [5, 5, 7, 6]
        self.correct_guess_int = 5512
        self.EASY_MAX = 5555
        self.MEDIUM_MAX = 7777
        self.HARD_MAX = 9999

    # @unittest.skip("working on function")
    def test_number_of_matches(self):
        self.assertEqual(mastermind.number_of_matches(self.key_list,
                                                      self.two_matches), "**")

    def test_numbers_are_equal(self):
        self.assertTrue(mastermind.numbers_are_equal(self.key_list,
                                                     self.correct_guess))
        self.assertFalse(mastermind.numbers_are_equal(self.key_list,
                                                      self.incorrect_guess))

    def test_convert_to_number(self):
        self.assertEqual(mastermind.convert_to_number(self.key_list),
                         self.correct_guess_int)

    def test_generate_number(self):
        for i in range(1000):
            # subTest() allows you to have each run as it's own test
            # useful when the tests just differ by parameter
            with self.subTest(i=i):
                self.assertTrue(mastermind.convert_to_number(
                    mastermind.generate_number("easy")) <= self.EASY_MAX)
                self.assertTrue(mastermind.convert_to_number(
                    mastermind.generate_number("medium")) <= self.MEDIUM_MAX)
                self.assertTrue(mastermind.convert_to_number(
                    mastermind.generate_number("hard")) <= self.HARD_MAX)
"""
Put expected failures here:
class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")
"""
import unittest
import mastermind


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
        test_status = False

        for i in range(1000):
            generated_value = \
                mastermind.convert_to_number(mastermind.generate_number("easy"))
            if generated_value > self.EASY_MAX:
                test_status = False
            else:
                test_status = True

        self.assertTrue(test_status)
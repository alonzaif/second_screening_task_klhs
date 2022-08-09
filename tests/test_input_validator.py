import unittest

from validator import input_validator


class TestInputValidator(unittest.TestCase):

    def test_not_in_format(self):
        self.assertRaises(ValueError, input_validator, '2022-08-01 08:00:01')

    def test_invalid_str(self):
        self.assertRaises(ValueError, input_validator, '2022-08-01 08:00 someextra')

    def test_date_not_exists(self):
        self.assertRaises(ValueError, input_validator, '2022-02-13 25:65')

    def test_output(self):
        date = '2022-08-01 08:00'
        expected_output = ['2022-08-01', '08:00']

        test_output = input_validator(date)

        self.assertEqual(expected_output, test_output)


if __name__ == '__main__':
    unittest.main()

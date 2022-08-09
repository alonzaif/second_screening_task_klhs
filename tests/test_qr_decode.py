import unittest

from QR_Reader import qr_decode


class TestDecoder(unittest.TestCase):

    def test_output_format(self):
        # qr_codes/1.png = 2022-08-01 08:00
        expected_output = '2022-08-01 08:00'
        test_output = qr_decode('../qr_codes/1.png')
        self.assertEqual(expected_output, test_output)


if __name__ == '__main__':
    unittest.main()

import unittest
from resources import actualparams


class MyTestCase(unittest.TestCase):
    def test_one_param(self):
        p1 = 'some   parameter'
        input_param = [p1]
        expect_param = '\\(\\"' + p1 + '\\"\\)'
        self.assertEqual(actualparams.create_actual_params(input_param), expect_param)

    def test_zero_param(self):
        p1 = ''
        input_param = [p1]
        self.assertEqual(actualparams.create_actual_params(input_param), '\\(\\"\\"\\)')

    def test_more_params(self):
        p1 = 'some   parameter'
        p2 = 12345,67
        p3 = 'a default value '
        p4 = 'New things'
        input_param = [p1, p2, p3, p4]
        expect_param = '\\(\\"' + p1 + '\\",\\"' + str(p2) + '\\",\\"' + \
                       p3 + '\\",\\"' + p4 + '\\"\\)'
        self.assertEqual(actualparams.create_actual_params(input_param), expect_param)


if __name__ == '__main__':
    unittest.main()

""" tests forward slashes are added """
import unittest

from resources.actualparams import create_actual_params


class ActualParamsTest(unittest.TestCase):
    """ General test"""
    def test_one_param(self):
        """ Simple one """
        p1 = 'some   parameter'
        input_param = [p1]
        expect_param = '\\(\\"' + p1 + '\\"\\)'
        self.assertEqual(create_actual_params(input_param), expect_param)

    def test_zero_param(self):
        """ Zero param test"""
        p1 = ''
        input_param = [p1]
        self.assertEqual(create_actual_params(input_param), '\\(\\"\\"\\)')

    def test_more_params(self):
        """ Multiple params test """
        p1 = 'some   parameter'
        p2 = 12345,67
        p3 = 'a default value '
        p4 = 'New things'
        input_param = [p1, p2, p3, p4]
        expect_param = '\\(\\"' + p1 + '\\",\\"' + str(p2) + '\\",\\"' + \
                       p3 + '\\",\\"' + p4 + '\\"\\)'
        self.assertEqual(create_actual_params(input_param), expect_param)


if __name__ == '__main__':
    unittest.main()

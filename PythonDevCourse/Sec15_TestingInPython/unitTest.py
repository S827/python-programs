import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self):  # default method that allows to run a piece of code that sets up before call of tests
        print('function testing will be started')

    def test_do_stuff(self):
        '''hii'''
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 60)

    def test_do_stuff2(self):
        test_param = 'sometext'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff5(self):
        test_param = 0
        result = main.do_stuff(test_param)
        self.assertEqual(result, 50)

    def test_power(self):
        test_param = 10
        result = main.power(test_param)
        self.assertEqual(result, 10000000000)

    def test_power2(self):
        test_param2 = 'some'
        result2 = main.power(test_param2)
        self.assertIsInstance(result2, ValueError)

    def tearDown(self):
        print('Cleaning Up')


if __name__ == '__main__':
    unittest.main()

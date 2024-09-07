import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self):
        print('Test has been started')

    def test_playGame(self):
        guess = 5
        num = 5
        result = main.playGame(guess, num)
        self.assertTrue(result)

    def test_wrong_guess(self):
        result = main.playGame(0, 5)
        self.assertFalse(result)

    def test_wrong_number(self):
        result = main.playGame(11, 5)
        self.assertFalse(result)

    def test_wrong_type(self):
        result = main.playGame('11', 5)
        self.assertFalse(result)

    def test_wrong_type_str(self):
        result = main.playGame('abc', 5)
        self.assertFalse(result)

    def tearDown(self):
        print('Cleaning Up')


if __name__ == '__main__':
    unittest.main()

# # sad
# def test_do_stuff(self):
#         '''hii'''
#         test_param = 10
#         result = main.do_stuff(test_param)
#         self.assertEqual(result, 60)

#     def test_do_stuff2(self):
#         test_param = 'sometext'
#         result = main.do_stuff(test_param)
#         self.assertIsInstance(result, ValueError)

#     def test_do_stuff3(self):
#         test_param = None
#         result = main.do_stuff(test_param)
#         self.assertEqual(result, 'please enter number')

#     def test_do_stuff4(self):
#         test_param = ''
#         result = main.do_stuff(test_param)
#         self.assertEqual(result, 'please enter number')

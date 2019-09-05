import unittest
import navigator

class testNavigationMethods(unittest.TestCase):

    def test_locate(self):
        self.assertEqual(navigator.locate(''), 0)
        self.assertEqual(navigator.locate('('), 1)
        self.assertEqual(navigator.locate('(('), 2)


# acceptance criteria

        # self.assertEqual(navigator.locate('(())'), 0)
        # self.assertEqual(navigator.locate('()()'), 0)
        # self.assertEqual(navigator.locate('((('), 3)


if __name__ == '__main__':
    unittest.main()

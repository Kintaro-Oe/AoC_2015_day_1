import unittest
import navigator

class testNavigationMethods(unittest.TestCase):

    def test_locate(self):
        self.assertEqual(navigator.locate(''), 0)

        # test floor increments
        self.assertEqual(navigator.locate('('), 1)
        self.assertEqual(navigator.locate('(('), 2)

        # test floor decrements
        self.assertEqual(navigator.locate(')'), -1)
        self.assertEqual(navigator.locate('))'), -2)

        # acceptance criteria
        self.assertEqual(navigator.locate('(())'), 0)
        self.assertEqual(navigator.locate('()()'), 0)
        self.assertEqual(navigator.locate('((('), 3)
        self.assertEqual(navigator.locate('))((((('), 3)
        self.assertEqual(navigator.locate('())'), -1)
        self.assertEqual(navigator.locate('))('), -1)
        self.assertEqual(navigator.locate(')))'), -3)
        self.assertEqual(navigator.locate(')())())'), -3)

    def test_position(self):
        self.assertEqual(navigator.position('()', 1), 1, 'test 1')
        self.assertEqual(navigator.position(')((', 1), 3, 'test 2')
        self.assertEqual(navigator.position(')((', 0), 0, 'test 3')



if __name__ == '__main__':
    unittest.main()

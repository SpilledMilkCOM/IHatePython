import unittest

from crafting.mockUtil import create_warrior

class TestStringMethods(unittest.TestCase):

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_warrior(self):
        test = create_warrior()

        self.assertIsNotNone(test)
        self.assertEqual(test.name, "He-Man")
        self.assertEqual(test.resources[0].name, "Water")
        self.assertEqual(test.resources[0].count, 100)

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
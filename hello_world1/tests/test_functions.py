from hello_world1.functions import hello_world1
import unittest


class TestHelloWorld1(unittest.TestCase):
    # property of assert function:
    # the number of characters shown in diff
    maxDiff = 1000

    def test_hello_world1(self):
        expected = "Hello World1!"
        actual = hello_world1()
        self.assertEqual(actual, expected)

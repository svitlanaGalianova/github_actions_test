from hello_world2.functions import hello_world2
import unittest


class TestHelloWorld1(unittest.TestCase):
    # property of assert function:
    # the number of characters shown in diff
    maxDiff = 1000

    def test_hello_world1(self):
        expected = "Hello World2!"
        actual = hello_world2()
        self.assertEqual(actual, expected)

    def test_hello_world_fail(self):
        expected = "Hello World2 - break!"
        actual = hello_world2()
        self.assertEqual(actual, expected)

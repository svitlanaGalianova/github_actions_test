from hello_world2.functions import hello_world2
import unittest


secret = ''

if secret == '':
    import os
    print(os.environ)
    secret = os.environ['SECRET_TEST']


class TestHelloWorld1(unittest.TestCase):
    # property of assert function:
    # the number of characters shown in diff
    maxDiff = 1000

    def test_hello_world1(self):
        expected = "Hello World2!"
        actual = hello_world2()
        self.assertEqual(actual, expected)

    def test_hello_world_fail(self):
        #expected = "I am wrong, this test will fail"
        actual = hello_world2()
        self.assertEqual(actual, secret)

from unittest import TestCase
import pte


class TestFunctionToTest(TestCase):
    def test_function_to_test(self):
        r = pte.todo_function_to_test(1, 2)
        print('Result=', r)
        assert r == 3

    def test_this_will_fail(self):
        r = pte.todo_function_to_test(1, 2)
        print('Result=', r)
        assert r == 4
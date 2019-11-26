from unittest import TestCase
import pte


class TestFunctionToTest(TestCase):
    def test_function_to_test(self):
        r = pte.todo_function_to_test(1, 2)
        assert r == 3

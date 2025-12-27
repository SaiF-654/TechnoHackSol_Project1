# myapp/tests.py
from django.test import TestCase

class SimpleTest(TestCase):
    def test_basic_math(self):
        self.assertEqual(1 + 1, 2)

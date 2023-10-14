from django.test import TestCase
from .main import sum2

def test_sum2():
    assert sum2(15, 8) == 23

# Create your tests here.

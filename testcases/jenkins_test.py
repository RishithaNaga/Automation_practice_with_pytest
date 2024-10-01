import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pageObjects.signup_and_login_page import Login
from .conftest import pytest_addoption
def test_one():
    print("hello world")
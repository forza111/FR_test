'''import requests
import pytest
from requests.auth import HTTPBasicAuth

API_URL = 'http://127.0.0.1:8000'
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin'

basicAuth = HTTPBasicAuth(ADMIN_PASSWORD, ADMIN_PASSWORD)

@pytest.fixture()
def some_data():
    """Return answer to ultimate question."""
    return 42

def test_some_data(some_data):
    """Use fixture return value in a test."""
    assert some_data == 42'''
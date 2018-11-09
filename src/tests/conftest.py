import pytest

from src import app

from src.binary_app import view


@pytest.fixture(scope='module')
def client():
    client = app.test_client()
 
    ctx = app.app_context()
    ctx.push()
 
    yield client
 
    ctx.pop()
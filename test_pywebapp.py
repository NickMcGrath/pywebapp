import json
import web
from pywebapp import app

b = app.browser()

def test_Default():
    b.open('/')
    assert 'A00931408' in b.get_text()

def test_Api():
    b.open('/api/v1/test')
    assert 'test' in b.get_text()

def test_ApiJson():
    b.open('/api/v1/json')
    result = json.loads(b.get_text())
    assert result['api-version'] == 'v1'

def test_ApiWorker():
    b.open('/api/v1/worker')
    result = json.loads(b.get_text())
    assert 'worker-name' in result

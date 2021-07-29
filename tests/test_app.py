import pytest
from fastapi.testclient import TestClient
from pytest import param
from requests.auth import HTTPBasicAuth

from toolip.fastapi import create_app_with_basic_auth

basic_auth_params = [
    param('USERNAME', 'X', '', '/openapi.json', 401, id='Openapi doc with wrong password'),
    param('X', 'PASSWORD', '', '/openapi.json', 401, id='Openapi doc with wrong username'),
    param(
        'USERNAME',
        'PASSWORD',
        '',
        '/openapi.json',
        200,
        id='Openapi doc with correct username and password',
    ),
    param('USERNAME', 'PASSWORD', '', '/docs', 200, id='Docs with correct username and password'),
    param(
        'USERNAME',
        'PASSWORD',
        '',
        '/redoc',
        200,
        id='Redoc with correct username and password',
    ),
    param('USERNAME', 'PASSWORD', '/api', '/openapi.json', 404, id='Openapi doc with wrong path'),
    param(
        'USERNAME',
        'PASSWORD',
        '/api',
        '/api/openapi.json',
        200,
        id='Openapi doc with correct path',
    ),
]


@pytest.mark.parametrize('username, password, prefix, path, status_code', basic_auth_params)
def test_add_api_doc_basic_auth(username, password, prefix, path, status_code):
    auth = HTTPBasicAuth(username=username, password=password)
    test_client = TestClient(app=create_app_with_basic_auth(prefix=prefix))
    for r in test_client.app.routes:
        print(r.path)
    response = test_client.get(path, auth=auth)
    print(response.text)
    assert response.status_code == status_code

import pytest
from fastapi import FastAPI
from pytest import param
from requests.auth import HTTPBasicAuth

from toolip.fastapi_tools import docs_behind_basic_auth, set_config

basic_auth_params = [
    param(
        'USERNAME',
        'X',
        'USERNAME',
        'Z',
        '',
        '/openapi.json',
        401,
        id='Openapi doc with wrong password'
    ),
    param(
        'X',
        'PASSWORD',
        'Z',
        'PASSWORD',
        '',
        '/openapi.json',
        401,
        id='Openapi doc with wrong username'
    ),
    param(
        'USERNAME',
        'PASSWORD',
        'USERNAME',
        'PASSWORD',
        '',
        '/openapi.json',
        200,
        id='Openapi doc with correct username and password',
    ),
    param(
        'USERNAME',
        'PASSWORD',
        'USERNAME',
        'PASSWORD',
        '',
        '/docs',
        200,
        id='Docs with correct username and password'
    ),
    param(
        'USERNAME',
        'PASSWORD',
        'USERNAME',
        'PASSWORD',
        '',
        '/redoc',
        200,
        id='Redoc with correct username and password',
    ),
    param(
        'USERNAME',
        'PASSWORD',
        'USERNAME',
        'PASSWORD',
        '/api',
        '/openapi.json',
        404,
        id='Openapi doc with wrong path'
    ),
    param(
        'USERNAME',
        'PASSWORD',
        'USERNAME',
        'PASSWORD',
        '/api',
        '/api/openapi.json',
        200,
        id='Openapi doc with correct path',
    ),
]


@pytest.mark.parametrize('conf_username, \
    conf_password, username, password, prefix, path, status_code', basic_auth_params)
def test_docs_behind_basic_auth(test_client, conf_username,
                                conf_password, username, password, prefix, path, status_code):
    auth = HTTPBasicAuth(username=username, password=password)
    set_config(username=conf_username, password=conf_password)
    docs_behind_basic_auth(app=test_client.app, prefix=prefix)
    response = test_client.get(path, auth=auth)
    assert response.status_code == status_code


app_params = [
    param(
        dict(),
        'docs_url, redoc_url, openapi_url',
        id='App with no doc url set to None',
    ),
    param(
        dict(app=FastAPI(docs_url=None)),
        'redoc_url, openapi_url',
        id='App with only docs url set to None',
    ),
    param(
        dict(docs_url=None, redoc_url=None),
        'openapi_url',
        id='App with openapi url not set to None',
    ),
    param(
        dict(redoc_url=None, openapi_url=None),
        'docs_url',
        id='App with docs url not set to None',
    ),
    param(
        dict(docs_url=None, openapi_url=None),
        'redoc_url',
        id='App with redoc url not set to None',
    ),
]


@pytest.mark.parametrize('test_app, doc_error', app_params, indirect=['test_app'])
def test_docs_behind_basic_auth_exception(test_app, doc_error):
    with pytest.raises(ValueError) as ex:
        docs_behind_basic_auth(app=test_app)
    assert doc_error in str(ex.value)

from secrets import compare_digest

from fastapi import APIRouter, Depends, FastAPI, HTTPException, status
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.openapi.utils import get_openapi
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from .config import Configuration
from .constants import DOCS_PATH, OPENAPI_PATH, REDOC_PATH

security = HTTPBasic()
_conf = Configuration(doc_username=None, doc_password=None)


def set_config(username: str, password: str) -> None:
    global _conf
    _conf = Configuration(doc_username=username, doc_password=password)


def doc_login(credentials: HTTPBasicCredentials = Depends(security)):
    if _conf.doc_username is not None and _conf.doc_password is not None:
        correct_username = compare_digest(credentials.username, _conf.doc_username)
        correct_password = compare_digest(credentials.password, _conf.doc_password)
        if not (correct_username and correct_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Incorrect username or password',
                headers={'WWW-Authenticate': 'Basic'},
            )
    return


def docs_behind_basic_auth(app: FastAPI, prefix: str = '') -> None:
    errors = [
        attr for attr in ['docs_url', 'redoc_url', 'openapi_url'] if getattr(app, attr) is not None
    ]
    if errors:
        raise ValueError(
            f'The following attributes must be set to None '
            f'when creating the FastAPI app: {", ".join(errors)}'
        )
    router = APIRouter()

    @router.get(OPENAPI_PATH, include_in_schema=False)
    async def get_open_api_endpoint():
        openapi_schema = get_openapi(
            title=app.title,
            version=app.version,
            description=app.description,
            routes=app.routes,
        )
        return JSONResponse(openapi_schema)

    app.openapi_url = f'{prefix}{OPENAPI_PATH}'

    @router.get(DOCS_PATH, include_in_schema=False)
    async def custom_swagger_ui_html():
        return get_swagger_ui_html(openapi_url=app.openapi_url, title=app.title + ' - Swagger UI')

    @router.get(str(app.swagger_ui_oauth2_redirect_url), include_in_schema=False)
    async def swagger_ui_redirect():
        return get_swagger_ui_oauth2_redirect_html()

    @router.get(REDOC_PATH, include_in_schema=False)
    async def redoc_html() -> HTMLResponse:
        return get_redoc_html(openapi_url=str(app.openapi_url), title=app.title + ' - ReDoc')

    # Disable authentication if no username and password is set
    if not _conf.doc_auth_is_on:
        app.include_router(router, prefix=prefix)
    else:
        app.include_router(router, prefix=prefix, dependencies=[Depends(doc_login)])

from typing import Optional

from pydantic import BaseSettings, validator


class Configuration(BaseSettings):
    doc_username: Optional[str] = ...  # type: ignore
    doc_password: Optional[str] = ...  # type: ignore

    @property
    def doc_auth_is_on(self):
        return self.doc_username is not None and self.doc_password is not None

    @validator('doc_username')
    def username_not_empty(cls, value):
        if value:
            return value
        return None

    @validator('doc_password')
    def password_not_empty(cls, value, values):
        username = values['doc_username']
        if value:
            if not username:
                raise ValueError('Username and Password should both be set')
            return value
        return None

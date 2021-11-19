from typing import Optional

from pydantic import BaseSettings, root_validator


class Configuration(BaseSettings):
    doc_username: Optional[str] = ...  # type: ignore
    doc_password: Optional[str] = ...  # type: ignore

    @property
    def doc_auth_is_on(self):
        return self.doc_username is not None and self.doc_password is not None

    @root_validator
    def check_creds(cls, values):
        username = values.get('doc_username')
        password = values.get('doc_password')
        if (username is None) ^ (password is None):
            raise ValueError('Username and Password should both be set or both not set')
        return values

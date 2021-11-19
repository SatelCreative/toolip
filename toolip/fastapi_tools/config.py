from typing import Optional

from pydantic import BaseSettings, root_validator


class Configuration(BaseSettings):
    doc_username: Optional[str] = None
    doc_password: Optional[str] = None

    @property
    def doc_auth_is_on(self):
        return self.doc_username is not None and self.doc_password is not None

    @root_validator
    def check_creds(cls, values):
        if ('doc_username' in values) ^ ('doc_password' in values):
            raise ValueError('Username and Password should both be set or both not set')
        return values

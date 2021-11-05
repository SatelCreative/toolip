from typing import Optional

from pydantic import BaseSettings, validator


class Configuration(BaseSettings):
    doc_username: Optional[str] = None
    doc_password: Optional[str] = None

    @property
    def doc_auth_is_on(self):
        return self.doc_username is not None and self.doc_password is not None

    @validator('doc_username')
    def username_not_empty(cls, value):
        if value and len(value) > 0:
           return value
        raise ValueError('Username must not be an empty string')

    @validator('doc_password')
    def password_not_empty(cls, value, values):
        username = values['doc_username']
        if value and len(value) > 0:
            if not username:
                raise ValueError('Username and Password should both be set')
            return value
        raise ValueError('Password must not be an empty string') 
    class Config:
        """Pydantic class to add prefix to properties defined."""

        env_prefix = 'API_'  # defaults to no prefix, i.e. ""


conf = Configuration()

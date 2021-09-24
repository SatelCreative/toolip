from enum import Enum

from pydantic import BaseSettings


class EnvironmentEnum(str, Enum):
    production = 'production'
    development = 'development'
    test = 'test'  # for pytest
    qa = 'qa'


class MainConfiguration(BaseSettings):
    environment: EnvironmentEnum = 'development'  # type: ignore
    public_domain: str = 'mydomain.satel.ca'
    sentry_environment: str = 'unknown'
    '''
    Sentry URL to server project, including key
    https://docs.sentry.io/error-reporting/configuration/
    '''
    sentry_dsn: str = ''

    @property
    def not_in_production(self) -> bool:
        return self.environment != EnvironmentEnum.production

    @property
    def in_test(self) -> bool:
        return self.environment == EnvironmentEnum.test

    @property
    def in_production(self) -> bool:
        return self.environment == EnvironmentEnum.production

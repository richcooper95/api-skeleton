import os

from typing import List, Type


basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    CONFIG_NAME = "base"
    USE_MOCK_EQUIVALENCY = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = "development"
    SECRET_KEY = os.getenv(
        "DEV_SECRET_KEY", "Super secret dev key..."
    )
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir}/app-dev.db"


class TestingConfig(BaseConfig):
    CONFIG_NAME = "test"
    SECRET_KEY = os.getenv("TEST_SECRET_KEY", "Super secret test key...")
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir}/app-test.db"


class ProductionConfig(BaseConfig):
    CONFIG_NAME = "production"
    SECRET_KEY = os.getenv("PROD_SECRET_KEY", "Super secret prod key...")
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir}/app-prod.db"


EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig,
    TestingConfig,
    ProductionConfig,
]

config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}

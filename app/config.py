import os

from typing import Type


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


def get_config(cfg_name: str) -> Type[BaseConfig]:
    """Get the config class corresponding to the given name.

    Arguments:
        cfg_name -- The config name.

    Returns:
        Type[BaseConfig] -- The config class.

    Raises:
        ValueError -- Unknown config name supplied.
    """
    if cfg_name == DevelopmentConfig.CONFIG_NAME:
        return DevelopmentConfig

    if cfg_name == TestingConfig.CONFIG_NAME:
        return TestingConfig

    if cfg_name == ProductionConfig.CONFIG_NAME:
        return ProductionConfig

    raise ValueError(f"Unknown config name: {cfg_name}")

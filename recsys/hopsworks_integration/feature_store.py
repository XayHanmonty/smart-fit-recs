import hopsworks
import pandas as pd

from loguru import logger
from recsys.config import settings


def get_feature_store():
    if settings.HOPSWORKS_API_KEY:
        logger.info("Loging to Hopsworks using HOPSWORKS_API_KEY env var.")
        project = hopsworks.login(
            api_key_value = settings.HOPSWORKS_API_KEY.get_secret_value()
        )
    else:
        logger.info("Login to Hopsworks using cached API key.")
        project = hopsworks.login()
    return project, project.get_feature_store() 
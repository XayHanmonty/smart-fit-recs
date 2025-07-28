import hopsworks
import pandas as pd

from loguru import logger
from recsys.config import settings
from hsfs import embedding
from recsys.hopsworks_integration import constants
from recsys.features.transactions import month_cos, month_sin


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


########################
#### Feature Groups ####
########################


def create_customers_feature_group(fs, df: pd.DataFrame, online_enabled: bool = True):
    customers_fg = fs.get_or_create_feature_group(
        name="customers",
        description="Customers data including age and postal code",
        version=1,
        primary_key=["customer_id"],
        online_enabled=online_enabled,
    )
    customers_fg.insert(df, wait=True)

    for desc in constants.customer_feature_descriptions:
        customers_fg.update_feature_description(desc["name"], desc["description"])

    return customers_fg


def create_articles_feature_group(
        fs,
        df: pd.DataFrame,
        articles_description_embedding_dim: int,
        online_enabled: bool = True,
):
    # Create the Embedding Index for the articles description embedding.
    emb = embedding.EmbeddingIndex()
    emb.add_embedding("embeddings", articles_description_embedding_dim)

    articles_fg = fs.get_or_create_feature_group(
        name="articles",
        version=1,
        description="Fashion items data including type of item, visual description and category",
        primary_key=["article_id"],
        online_enabled=online_enabled,
        features=constants.article_feature_description,
        embedding_index=emb,
    )
    articles_fg.insert(df, wait=True)

    return articles_fg


def create_transactions_feature_group(
        fs, df: pd.DataFrame, online_enabled: bool = True
):
    trans_fg = fs.get_or_create_feature_group(
        name="transactions",
        version=1,
        description="Transactions data including customer, item, price, sales channel and transaction date",
        primary_key=["customer_id", "article_id"],
        online_enabled=online_enabled,
        transformation_functions=[month_sin, month_cos],
        event_time="t_dat",
    )
    trans_fg.insert(df, wait=True)

    for desc in constants.transactions_feature_descriptions:
        trans_fg.update_feature_description(desc["name"], desc["description"])

    return trans_fg


def create_interactions_feature_group(
        fs, df: pd.DataFrame, online_enabled: bool = True
):
    interactions_fg = fs.get_or_create_feature_group(
        name="interactions",
        version=1,
        description="Customer interactions with articles including purchases, clicks, and ignores. Used for building recommendation systems and analyzing user behavior.",
        primary_key=["customer_id", "article_id"],
        online_enabled=online_enabled,
        event_time="t_dat",
    )

    interactions_fg.insert(
        df,
        wait=True,
    )

    for desc in constants.interactions_feature_descriptions:
        interactions_fg.update_feature_description(desc["name"], desc["description"])

    return interactions_fg


# Create feature group for ranking
def create_ranking_feature_group(
    fs, df: pd.DataFrame, parents: list, online_enabled: bool = True
):
    rank_fg = fs.get_or_create_feature_group(
        name="ranking",
        version=1,
        description="Derived feature group for ranking",
        primary_key=["customer_id", "article_id"],
        parents=parents,
        online_enabled=online_enabled,
    )
    rank_fg.insert(df, wait=True)

    for desc in constants.ranking_feature_descriptions:
        rank_fg.update_feature_description(desc["name"], desc["description"])

    return rank_fg




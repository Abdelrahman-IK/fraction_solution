import pandas as pd
from sqlalchemy import create_engine


DB_CONN = "postgresql://user:1234@db:5432/postgres"
ENGINE = create_engine(DB_CONN)


def load_users(users_dataframe: pd.DataFrame) -> None:
    """
    Load users dataframe into the DB table
    Input:
        users_dataframe: A pandas dataframe that contains users info
    returns:
        None
    """
    users_dataframe.to_sql('user', ENGINE, if_exists='append',index=False)


def load_properties(properties_dataframe: pd.DataFrame) -> None:
    """
    Load properties dataframe into the DB table
    Input:
        properties_dataframe: A pandas dataframe that contains properties info
    returns:
        None
    """
    properties_dataframe.to_sql('property', ENGINE, if_exists='append',index=False)


def load_events(events_dataframe: pd.DataFrame) -> None:
    """
    Load events dataframe into the DB table
    Input:
        events_dataframe: A pandas dataframe that contains events info
    returns:
        None
    """
    events_dataframe.to_sql('event', ENGINE, if_exists='append',index=False)

import json
import pandas as pd

def transform_users(users_file: str) -> pd.DataFrame:
    """
    Transforming users into a cleaned dataframe

    input:
        users_file: a location for the json file that contains users
    returns:
        pandas dataframe
    """
    with open(users_file) as f:
        data = json.load(f)
    frame = pd.DataFrame(data)
    frame = pd.concat([frame, pd.DataFrame(list(frame['address'].apply(lambda x: x.split(","))), columns=["street","city", "state","country", "postal"])], axis=1)
    del frame['address']
    frame['street'] = frame['street'].apply(lambda x: x.replace(' - ','') if x.startswith(' -') else x)
    return frame


def transform_properties(properties: str) -> pd.DataFrame:
    """
    Transforming properties into a cleaned dataframe

    input:
        properties: a location for the csv file that contains properties
    returns:
        pandas dataframe
    """
    dataframe = pd.read_csv(properties)
    dataframe[['postal','state']] = dataframe[['state','postal']]
    return dataframe

print(transform_properties('data/properties.csv'))
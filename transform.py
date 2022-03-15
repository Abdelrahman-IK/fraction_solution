import json
import pandas as pd
import glob
import ast
import re

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


def extract_logs_data(data: str) -> dict:
    """
    Extracting the dictionary logs data from the text

    input:
        data: text that contains dictionary data
    returns:
        dictionary
    """
    try:
        return ast.literal_eval(re.search('({.+})', data).group(0))
    except:
        return { "email": None, "type": None, "message": None}


def transform_logs(logs_dir: str) -> pd.DataFrame:
    """
    Transforming text logs files into a cleaned dataframe

    input:
        logs_dir: a location for the directory of logs
    returns:
        pandas dataframe
    """
    frame = pd.DataFrame()
    for file in glob.glob(logs_dir+"*.txt"):
        with open(file) as f:
            data = f.read()
        df = pd.DataFrame(data.split('\n'),columns=['logs'])
        df['timestamp'] = df['logs'].apply(lambda x: x.split(' GMT')[0])
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['data'] = df['logs'].apply(lambda x: extract_logs_data(x))
        df = pd.concat([df,df['data'].apply(pd.Series)], axis=1)
        del df['logs']
        del df['data']
        frame = frame.append(df)
    frame = frame.dropna()
    return frame

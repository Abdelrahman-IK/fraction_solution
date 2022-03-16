import pandas as pd


def run(properties_file: str) -> None:
    """
    Testing the properties data
    """
    dataframe = pd.read_csv(properties_file)

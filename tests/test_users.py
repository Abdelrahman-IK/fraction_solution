import json
import pandas as pd

def run(users_file: str) -> None:
    """
    Testing the users data
    """
    with open(users_file) as f:
        data = json.load(f)
    frame = pd.DataFrame(data)

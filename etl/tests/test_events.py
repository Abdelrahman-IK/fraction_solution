import glob


def run(events_dir: str) -> None:
    """
    Testing the events data
    """
    for file in glob.glob(events_dir+"*.txt"):
        with open(file) as f:
            f.read()

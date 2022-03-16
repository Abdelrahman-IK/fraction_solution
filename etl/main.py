import transform
import load
from tests import (
    test_events, 
    test_properties, 
    test_users)

USERS_FILE = 'data/users.json'
PROPERTIES_FILE = 'data/properties.csv'
EVENTS_DIR = 'data/events/'

def run_tests():
    test_users.run(USERS_FILE)
    test_properties.run(PROPERTIES_FILE)
    test_events.run(EVENTS_DIR)


if __name__ == '__main__':
    run_tests()
    transformed_user_data = transform.transform_users(USERS_FILE)
    load.load_users(transformed_user_data)
    transformed_properties_data = transform.transform_properties(PROPERTIES_FILE)
    load.load_properties(transformed_properties_data)
    transformed_events_data = transform.transform_logs(EVENTS_DIR)
    load.load_events(transformed_events_data)

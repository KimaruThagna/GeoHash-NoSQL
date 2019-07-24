import json
from add_retrieve_db import *

# data is what is retrieved from the db. test_data is known to been have entered in the db.
# test and assert if this data is the same.
with open("data/grocery_json_list_test.json","r") as file_obj:
    test_data = json.load(file_obj)


def test_data_from_dynamoDB():

    assert data == test_data
    assert len(data) == len(test_data)

import boto3,json
from simple_geohash import *
from boto3.dynamodb.conditions import Attr,Key
dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

class DynamoDBCommunicator():
    groceries_table=dynamodb.Table('Grocery_stores')
    def add_to_dynamodb(self,item):
        grocery_stores.put_item(
            Item={
                  "id":item["id"],
                  "name":item["name"],
                  "geohash":Geohash.encode(item["location"][0], item["location"][1])

            }
        )
        return f'Item {item["name"]} has been added succesfully '

    def retrieve_from_dynamodb(self):
        pe = 'id, name, geohash'

        response = self.groceries_table.scan(
            # what we are retrieving from DB
            ProjectionExpression=pe,

        )
        Items = []
        if response["Items"]:

            for i in response['Items']:
                Items.append(json.loads(json.dumps(i)))
            return Items

        else:
            return "No Items in the DB"


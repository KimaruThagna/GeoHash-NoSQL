import boto3,json,decimal
from simple_geohash import *
from boto3.dynamodb.conditions import Attr,Key
dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

class DynamoDBCommunicator():
    groceries_table=dynamodb.Table('Grocery_stores')
    def add_to_dynamodb(self,item):
        self.groceries_table.put_item(
            Item={
                  "id":item["id"],
                  "name":item["name"],
                  "geohash":Geohash.encode(item["location"][0], item["location"][1])

            }
        )
        return f'Item {item["name"]} has been added succesfully '

    def retrieve_from_dynamodb(self):
        pe = 'id, #grocery_store_name, geohash'
        ean = {"#grocery_store_name": "name", }

        response = self.groceries_table.scan(
            # what we are retrieving from DB
            ProjectionExpression=pe,
            ExpressionAttributeNames=ean, # used when you want to substitute your data

        )
        Items = []
        if response["Items"]:

            for i in response['Items']:
                Items.append(json.loads(json.dumps(i, cls=DecimalEncoder)))
            return Items

        else:
            return "No Items in the DB"

db_communicator_obj = DynamoDBCommunicator()
# add data to db
# for store in grocery_stores:
#     print(db_communicator_obj.add_to_dynamodb(store))

# retrieve from dynamodb, geohash decode and store result in json_file
data = db_communicator_obj.retrieve_from_dynamodb()

with open("data/grocery_json_list.json","w") as file_obj:

    file_obj.write(str(data))

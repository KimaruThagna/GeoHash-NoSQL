import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

def deleteTable():
    table=dynamodb.Table('Grocery_stores')
    print('deleting table')
    print(">>>>>>>>>>>>>>>>>>>>>.done")
    return table.delete()



def create_table():

    table = dynamodb.create_table(
        TableName='Grocery_stores',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'  #Partition key
            },
            {
                'AttributeName': 'geohash',
                'KeyType': 'RANGE'  #Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'geohash',
                'AttributeType': 'S'
            },


        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    return print("Table status:", table.table_status)

create_table()
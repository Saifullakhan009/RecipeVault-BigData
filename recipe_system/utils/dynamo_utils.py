import boto3
from botocore.exceptions import ClientError

# Initialize DynamoDB
dynamodb = boto3.resource("dynamodb", endpoint_url="http://localhost:4566")  # Replace with LocalStack's endpoint
table_name = "RecipeMetadata"

# Create DynamoDB table
def initialize_dynamodb_table():
    try:
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[{"AttributeName": "recipe_id", "KeyType": "HASH"}],
            AttributeDefinitions=[{"AttributeName": "recipe_id", "AttributeType": "S"}],
            ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        )
        table.wait_until_exists()
    except ClientError as e:
        if e.response["Error"]["Code"] != "ResourceInUseException":
            raise

# Add metadata for a recipe
def add_recipe_metadata(recipe_id, views, likes, tags):
    table = dynamodb.Table(table_name)
    table.put_item(Item={"recipe_id": recipe_id, "views": views, "likes": likes, "tags": tags})

# Retrieve metadata for a recipe
def get_recipe_metadata(recipe_id):
    table = dynamodb.Table(table_name)
    response = table.get_item(Key={"recipe_id": recipe_id})
    return response.get("Item", {})

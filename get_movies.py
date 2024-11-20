# Function that fetches all movies from DynamoDB and returns their
# details including the cover image URL from S3

import boto3
import json
from decimal import Decimal

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Movies')

    # scan the table to fetch all items
    response = table.scan()
    movies = response.get('Items', [])

    # return the result
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(movies, default=decimal_default)
    }

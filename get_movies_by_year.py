# Function that fetches movies relesed in a specific year

import boto3
import json
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Movies')

    # Extract year from event
    year = None
    if 'queryStringParameters' in event and event['queryStringParameters'] is not None:
        year = event['queryStringParameters'].get('year')  # For API Gateway
    elif 'year' in event:
        year = event['year']  # For direct testing

    if not year:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing 'year' parameter."})
        }

    # Query DynamoDB for movies by year
    response = table.scan()
    movies = response.get('Items', [])
    filtered_movies = [movie for movie in movies if int(movie['releaseYear']) == int(year)]

    return {
        "statusCode": 200,
        "body": json.dumps(filtered_movies, cls=DecimalEncoder)
    }
# Importing libraries
import json
import random

def lambda_handler(event, context):
    # Generate a random number from 1 to 6
    random_number = random.randint(1, 6)
    
    # Return the result as a JSON object
    return {
        'statusCode': 200,
        'body': f'Random number: {random_number}'
    }

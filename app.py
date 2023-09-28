# Імпорт бібліотек
import json
import random

def lambda_handler(event, context):
    # Генеруємо випадкове число від 1 до 6
    random_number = random.randint(1, 6)
    
    # Повертаємо результат у вигляді об'єкта JSON
    return {
        'statusCode': 200,
        'body': f'<p>Випадкове число: {random_number}</p>'
    }

# ������ �������
import json
import random

def lambda_handler(event, context):
    # �������� ��������� ����� �� 1 �� 6
    random_number = random.randint(1, 6)
    
    # ��������� ��������� � ������ ��'���� JSON
    return {
        'statusCode': 200,
        'body': f'<p>��������� �����: {random_number}</p>'
    }

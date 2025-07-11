import json
import boto3
import random

sqs_client = boto3.client('sqs')
sqs_queue_url = 'https://sqs.eu-north-1.amazonaws.com/178070228754/sqs-for-bulk-msgs'

def generate_sales_order():
    sales_order = {
        'sales_order_id': random.randint(1000, 9999),
        'customer_name': random.choice(['Customer A', 'Customer B', 'Customer C']),
        'total_amount': round(random.uniform(1000, 10000), 2)
    }
    return sales_order


def lambda_handler(event, context):
    i=0
    while i<150:
        sales_order = generate_sales_order()
        print(sales_order)
        sqs_client.send_message(
           QueueUrl=sqs_queue_url,
          MessageBody=json.dumps(sales_order)
        )
        i=i+1
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

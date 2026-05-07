import json
import boto3

ses = boto3.client('ses', region_name='us-east-1')

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        name    = body.get('name', 'No name')
        email   = body.get('email', 'No email')
        message = body.get('message', 'No message')

        ses.send_email(
            Source='oluwatunmikeolusoga@gmail.com',
            Destination={'ToAddresses': ['oluwatunmikeolusoga@gmail.com']},
            Message={
                'Subject': {'Data': f'New contact from {name}'},
                'Body': {'Text': {'Data': f'Name: {name}\nEmail: {email}\nMessage: {message}'}}
            }
        )

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST,OPTIONS'
            },
            'body': json.dumps({'message': 'Email sent'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }

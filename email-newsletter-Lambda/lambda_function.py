import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Attr
from datetime import datetime, timedelta

dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="https://dynamodb.us-east-1.amazonaws.com")
subscriptions_table = dynamodb.Table('test')

AWS_REGION = "us-east-1"
SUBJECT = "newsApp - newsletter"
CHARSET = "UTF-8"

def handler(json_input, context):
    news = []
    #get all subscribers
    subscribers = subscriptions_table.scan(
        AttributesToGet=['email']
    )
    #send a newsletter to each subscriber
    print(len(subscribers['Items']))
    for subscriber in subscribers['Items']:
        send_newsletter_report_to_address(subscriber['email'], news)


def send_newsletter_report_to_address(email_address, news):
    global AWS_REGION, SUBJECT, CHARSET
    body_html, body_text = compose_weekly_report_body(news)
    client = boto3.client('ses', region_name=AWS_REGION)
    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    email_address,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': body_html,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': body_text,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source="allexandra.gadioi@gmail.com",
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['ResponseMetadata']['RequestId'])


#receives news, returns the html body of the email message to be sent (and the text body, for non-HTML email clients)
def compose_weekly_report_body(news):
    text_body = "text - test from newsApp team"
    html_body = "html - test from newsApp team"
    return html_body, text_body

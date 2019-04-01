import boto3
from botocore.exceptions import ClientError
import json
from botocore.vendored import requests

dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="https://dynamodb.us-east-1.amazonaws.com")
subscriptions_table = dynamodb.Table('test')

AWS_REGION = "us-east-1"
SUBJECT = "newsApp - newsletter"
CHARSET = "UTF-8"

def handler(json_input, context):
    #get all subscribers
    subscribers = subscriptions_table.scan(
        AttributesToGet=['email']
    )
    # get news
    news = get_news()
    #send a newsletter to each subscriber
    print(len(subscribers['Items']))
    for subscriber in subscribers['Items']:
        send_newsletter_report_to_address(subscriber['email'], news)


def send_newsletter_report_to_address(email_address, news):
    global AWS_REGION, SUBJECT, CHARSET
    body_html, body_text = compose_report_body(news)
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
def compose_report_body(news):
    text_body = "text"
    html_body = """<html>
    <head>
        <style>
        </style>
    </head>
    <body>
      <h3>newsApp - newsletter</h3>
      <p>Most recent news:</p>
      """
    for article in news:
        html_body += "<h1>" + article['title'] + "</h1><small>Publish date: " + \
        article['publishedDate'] + "</small><br><a href=" + article['link'] + ">go to article</a><h3>" + article['summary'] + \
            "</h3><p>" + article['content'] + "</p>"
    html_body += "</body></html>"
    return html_body, text_body


def get_news():
    url = 'http://newsapp.syvh7ndmiz.eu-central-1.elasticbeanstalk.com/news'
    r = requests.get(url)
    return json.loads(r.text)

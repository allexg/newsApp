import boto3

translate = boto3.client(service_name='translate', region_name='region', use_ssl=True,
                    aws_access_key_id="******************************",
                    aws_secret_access_key="************************")

result = translate.translate_text(Text="Hello, World",
            SourceLanguageCode="en", TargetLanguageCode="de")
print('TranslatedText: ' + result.get('TranslatedText'))
print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))
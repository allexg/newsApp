import boto3

translate = boto3.client(service_name='translate', region_name='eu-central-1', use_ssl=True,
                    aws_access_key_id="AKIATIJQG3LSDOFM2UML",
                    aws_secret_access_key="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")

result = translate.translate_text(Text="Hello, World",
            SourceLanguageCode="en", TargetLanguageCode="de")
print('TranslatedText: ' + result.get('TranslatedText'))
print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))
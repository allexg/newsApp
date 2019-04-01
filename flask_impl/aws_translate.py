import boto3

def translate_text(text, language):
    translate = boto3.client(service_name='translate', region_name='eu-central-1', use_ssl=True,
                        aws_access_key_id="******************",
                        aws_secret_access_key="***********************")
    result = translate.translate_text(Text=text,
                SourceLanguageCode="en", TargetLanguageCode=language)
    return result.get('TranslatedText')


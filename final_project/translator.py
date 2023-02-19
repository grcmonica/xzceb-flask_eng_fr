import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('ApS3brax_bzS1eQECQZKDFd6ZGBew2eyik5Pi1ea3iV5')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/2da8f2a5-c6ef-43ad-8075-d9ccfcc4b84b')

translation = language_translator.translate(
    text='Bonjour',
    model_id='fr-en').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

"""file to perform translation tasks"""


def get_authentificator_from_ibm_watson(api_key, api_url):
    """methd to get authentifcation credentials fom IBM LAnguage Translator"""

    authenticator = IAMAuthenticator(api_key)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url(api_url)

    return language_translator

def english_to_french(english_text):
    """function to translate from english to french"""
    if not english_text:
        return "Nothing to translate"
    translation = get_authentificator_from_ibm_watson(apikey, url).translate(
        text=english_text,
        model_id='en-fr').get_result()

    return translation["translations"][0]["translation"]

def french_to_english(french_text):
    """function to translate from french to english"""
    if not french_text:
        return "Nothing to translate"
    translation = get_authentificator_from_ibm_watson(apikey, url).translate(
        text=french_text,
        model_id='fr-en').get_result()

    return translation["translations"][0]["translation"]

"""Translator Engine"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator("42fRjeeM6UbHeqJZLGS9mrwr5MG9lbkNjgFPN7z71Wpx")
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)


language_translator.set_service_url(
    "https://api.eu-de.language-translator.watson.cloud.ibm.com/instances/3664aa9c-eca0-4dec-95cb-d3e3468a2b8c")

def english_to_french(text_1):
    """
    This function translates english to french
    """
    #write the code here
    frenchtranslation = language_translator.translate(
        text= text_1,
        model_id='en-fr'
    ).get_result()
    return frenchtranslation.get("translations")[0].get("translation")

def french_to_english(text_1):
    """
    This function translates french to english
    """
    #write the code here
    englishtranslation = language_translator.translate(
        text= text_1,
        model_id='fr-en'
    ).get_result()
    return englishtranslation.get("translations")[0].get("translation")

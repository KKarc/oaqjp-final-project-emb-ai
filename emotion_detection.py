import requests
import json

def emotion_detector(text_to_analyse: str) -> str:
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    analyse_input = { "raw_document": { "text": text_to_analyse} }

    response = requests.post(url, json=analyse_input, headers=headers)

    formatted_response = json.loads(response.text)

    return str(formatted_response)
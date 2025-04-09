import requests
import json

def emotion_detector(text_to_analyze: str) -> str:
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    analyse_input = { "raw_document": { "text": text_to_analyze} }

    response = requests.post(url, json=analyse_input, headers=headers)

    formatted_response = json.loads(response.text)
    print(response.status_code)
    if response.status_code == 400:
        emotion_dict = {"anger": None,
                            "disgust": None,
                            "fear": None,
                            "joy": None,
                            "sadness": None,
                            "dominant_emotion": None}
    elif response.status_code == 200:
        #cleaning the dictionary to only include emotions and their scores
        emotion_dict = formatted_response['emotionPredictions'][0]['emotion']
        #adding dominant emotion to the response dictionary
        emotion_dict['dominant_emotion']=list(emotion_dict.keys())[list(emotion_dict.values()).index(max(emotion_dict.values()))]
    
    return emotion_dict
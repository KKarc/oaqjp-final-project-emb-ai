"""The program runs emotion detection on user input"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    """defining the app to run emotion detection on input data"""
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'
    #initiate output string variable
    output_str = "For the given statement, the system response is "
    #iterate through emotions and their scores
    for key, value in response.items():
        if key != 'dominant_emotion':
            output_str += f"'{key}': {value}, "
    #remove the trailing comma and space, add a period.
    output_str = output_str[:-2] + "."
    #add dominant emotion
    output_str += f" The dominant emotion is {response['dominant_emotion']}."
    return output_str

@app.route("/")
def render_index_page():
    """rendering the index page"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

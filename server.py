"""Flask application for emotion detection using Watson NLP."""

from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Endpoint to detect the emotion of a given text.

    Query Parameters:
        text (str): Text input to analyze emotions.

    Returns:
        str: Formatted string with emotion scores and dominant emotion
             or an error message for invalid input.
    """
    text_to_analyse = request.args.get('text')

    # Call the emotion_detector function
    response = emotion_detector(text_to_analyse)

    # Handle invalid input
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format response string
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


if __name__ == "__main__":
    # Run the Flask application on localhost:5000
    app.run(host="localhost", port=5000, debug=True)

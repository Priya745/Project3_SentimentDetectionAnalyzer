from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)


def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    polarity = sentiment.polarity             # from -1 to 1

    if polarity > 0:
        sentiment_category = "Positive"
    elif polarity < 0:
        sentiment_category = "Negative"
    else:
        sentiment_category = "Neutral"

    return sentiment_category

@app.route('/', methods=["GET", "POST"])
def index():
    sentiment = None

    if request.method == 'POST':
        text = request.form['text']
        sentiment = analyze_sentiment(text)

    return render_template('index.html', sentiment=sentiment)

@app.route('/about')
def about():
    return (render_template('about.html'))


@app.route('/contact')
def contact():
    return (render_template('contact.html'))


if __name__ == '__main__':
    app.run(debug=True)
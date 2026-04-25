from flask import Flask, request, render_template_string

app = Flask(__name__)

html = '''
<h1>Sentiment Analysis App</h1>
<form method="post">
<input type="text" name="text" placeholder="Enter text">
<button type="submit">Check</button>
</form>
{% if result %}
<h2>{{ result }}</h2>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    if request.method == 'POST':
        text = request.form['text'].lower()
        positive = ['good', 'great', 'love', 'happy', 'excellent']
        negative = ['bad', 'hate', 'sad', 'poor', 'worst']

        if any(word in text for word in positive):
            result = "Positive"
        elif any(word in text for word in negative):
            result = "Negative"
        else:
            result = "Neutral"

    return render_template_string(html, result=result)

app.run(host="0.0.0.0", port=5000)

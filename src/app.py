from flask import Flask, render_template, request
import re

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    regex_result = ""
    if request.method == 'POST':
        pattern = request.form['pattern']
        text = request.form['text']
        try:
            regex_result = re.findall(pattern, text)
            regex_result = ', '.join(regex_result)
        except re.error:
            regex_result = "Invalid regex pattern"
    return render_template('index.html', regex_result=regex_result)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000, debug=True)

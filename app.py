from flask import Flask, render_template, request
import openai


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        input = request.form['userInput']
        prompt = request.form['prompt']

        print(input + prompt)
    return render_template('template.html')


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import openai


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():

    return render_template('template.html')


if __name__ == '__main__':
    app.run(debug=True)

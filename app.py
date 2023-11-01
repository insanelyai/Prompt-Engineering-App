from flask import Flask, render_template, request
import openai

openai.api_key = "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-ctchp"

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        input = request.form['userInput']
        prompt = request.form['prompt']

        post_req = input + " " + prompt

        # ChatGPT Training Model
        model_engine = "text-davinci-002"
        completions = openai.Completion.create(
            engine=model_engine,
            prompt=post_req,
            max_tokens=100,
        )

        # Get the response
        get_res = completions.choices[0].text.strip()

        fetched_data = get_res
        return render_template('template.html', fetched_data=fetched_data)
    else:
        return render_template('template.html')


if __name__ == '__main__':
    app.run(debug=True)

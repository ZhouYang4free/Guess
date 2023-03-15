from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key = "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"


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        question = request.form['question']
        answer = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"I have a question: {question}\n\nAnswer:",
            temperature=0.5,
            max_tokens=50,
            n=1,
            stop=None,
            timeout=10,
        )

        return render_template('index.html', answer=answer.choices[0].text)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
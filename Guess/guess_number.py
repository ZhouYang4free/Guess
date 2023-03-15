from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import random


app = Flask(__name__)
CORS(app)


def generate_answer():
    return random.randint(1, 100)


answer = generate_answer()
guess_count = 0


@app.route('/guess', methods=['GET', 'POST'])
def guess():
    global answer, guess_count
    if request.method == 'POST':
        guess_number = int(request.json['guess'])
        if guess_number == answer:
            answer = generate_answer()
            guess_count += 1
            return jsonify({'result': 'equal', 'answer': answer, 'guess_count': guess_count})
        elif guess_number > answer:
            result = 'larger'
        else:
            result = 'smaller'
        guess_count += 1
        return jsonify({'result': result})
    else:
        return render_template('index.html')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all():
    return "Page not found"


if __name__ == '__main__':
    app.run(port=5000)

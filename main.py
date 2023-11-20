from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html'),render_template('main.css'),render_template('logo.png')


@app.route('/sample')
def sample():
    return 'This is a sample endpoint.'


if __name__ == '__main__':
    app.run(debug=True)

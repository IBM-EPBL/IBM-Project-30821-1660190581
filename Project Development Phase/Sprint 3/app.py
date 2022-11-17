from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/chance')
def chance():
    return render_template('chance.html')

@app.route('/noChance')
def noChance():
    return render_template('noChance.html')


if __name__ == "__main__":
    app.run()

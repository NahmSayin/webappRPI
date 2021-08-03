from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/levels')
def levels():
    return render_template('levels.html')

@app.route('/level1exercise')
def level1exercise():
    return render_template('level1exercise.html')

@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')

@app.route('/progress/<name>')
def progress(name):
    return render_template('progress.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


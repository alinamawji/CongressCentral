# main.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
@app.route('/members.html/index.html/')
def index():
    return render_template('index.html')

@app.route('/members.html/', methods=['GET'])
def members():
    return render_template('members.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port = 8080)
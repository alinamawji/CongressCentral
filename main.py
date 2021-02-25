# application.py
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# MEMBERS
@app.route('/members/', methods=['GET'])
def members():
    return render_template('members.html')

@app.route('/members/baldwin')
def baldwin():
    return render_template('baldwin.html')

@app.route('/members/barrasso')
def barrasso():
    return render_template('barrasso.html')

@app.route('/members/bennet')
def bennet():
    return render_template('bennet.html')

@app.route('/members/blackburn')
def blackburn():
    return render_template('blackburn.html')

@app.route('/members/blumenthal')
def blumenthal():
    return render_template('blumenthal.html')

@app.route('/members/blunt')
def blunt():
    return render_template('blunt.html')

@app.route('/members/booker')
def booker():
    return render_template('booker.html')

@app.route('/members/boozman')
def boozman():
    return render_template('boozman.html')

@app.route('/members/braun')
def braun():
    return render_template('braun.html')

@app.route('/members/brown')
def brown():
    return render_template('brown.html')

@app.route('/committees/')
def committees():
    return render_template('committees.html')

@app.route('/legislation/')
def legislation():
    return render_template('legislation.html')

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port = 8080)
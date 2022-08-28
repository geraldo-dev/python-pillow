from flask import Flask, render_template, request
# from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

if __name__=='__main__':
    app.run()
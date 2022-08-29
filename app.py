import os
from flask import Flask, render_template, request
from datetime import datetime
from PIL import Image

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        img = request.files['img']
        options = request.form['options']
        name = request.form['name']
        
        if img and (options  != 'escolha'):
            new_image = Image.open(img, 'r')

            if options == 'png':
                
                new_image.save(name + ".png")
            elif options == 'jpg':
                new_image.save(name + ".jpg")
            elif options == 'jpeg':
                new_image.save(name + ".jpeg")
            else:
                msg = 'invalid format'
                return render_template('index.html', msg=msg)
                
        msg = 'successfully converted'
        return render_template('index.html', msg=msg)
    
    success = "choose image and format"
    return render_template('index.html', success=success)


if __name__=='__main__':
    app.run()
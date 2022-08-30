from hashlib import new
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
        
        if img and (options  != 'escolha'):
            new_image = Image.open(img, 'r')
            name = str(img.filename.split('.')[0])
            #folde name
            folde = "C:\\Users\\Dell\\Documents\\image-converter\\new_image\\"

            if options == 'png':
                new_image.save(folde + name + ".png")
            elif options == 'jpg':
                new_image.save(folde + name + ".jpg")
            elif options == 'jpeg':
                new_image.save(folde + name + ".jpeg")
            else:
                msg = 'invalid format'
                return render_template('index.html', msg=msg)
                
        success = 'successfully converted'
        return render_template('index.html', success=success)
    
    return render_template('index.html')


if __name__=='__main__':
    app.run()
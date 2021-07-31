import sys
import os
import re
import json
from flask import *
from werkzeug.utils import secure_filename
from preprocessing import preprocessing

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploaded', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      image_text = preprocessing(f.filename)

      # trim_from_first = a.index('DESCRIPTION ‘QUANTITY PRICE SALES TAX AMOUNT')
      
      # trim_from_last = a.index('SUBTOTAL: $10.00')

      # a = a[trim_from_first:]
      # a = a[:trim_from_last]

      # headings = str(a[0])
      
      # headings = list(headings.split(' '))
      
      # a.pop(0)
      
      # row = []
      # for i in range(len(a)):
          
      #   d = str(a[i])
      #   row.append(list(d.split(' ')))
    
      # row = str(a[0])
      # row = list(row.split(' '))

      
    

      # extract_info = dict(zip(headings, row))



    #   return render_template('index.html', message = 'upload succesfull',headings = headings,rows=row)
      return render_template('index.html', message = 'upload succesfull',result =a)

if __name__ == '__main__':
    app.run(debug=True)

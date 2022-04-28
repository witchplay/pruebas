
from flask import Flask , render_template

import os


app= Flask(__name__)

_port = os.environ.get('PORT', 5000)

@app.route('/')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run()
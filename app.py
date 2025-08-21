import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

GUIDELINES_FOLDER = os.path.join('static', 'guidelines')

@app.route('/')
def index():
    files = os.listdir(GUIDELINES_FOLDER)
    return render_template('index.html', files=files)

@app.route('/guidelines/<filename>')
def serve_file(filename):
    return send_from_directory(GUIDELINES_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)

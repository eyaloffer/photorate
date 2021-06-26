from flask import Flask,render_template,request
import os
from pathlib import Path
import json

f = open('config.json',)
config = json.loads(f.read())
f.close()
photos_folder = config['photos_path']
base_folder = os.path.split(photos_folder)
unsort_folder = base_folder[1]
base_folder = base_folder[0]
for folder in ['no', 'maybe', 'yes']:
    Path(base_folder + '/' + folder).mkdir(parents=True, exist_ok=True)
app = Flask(__name__,static_folder=base_folder)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/unsorted')
def unsorted():
    hists = os.listdir(photos_folder)
    hists = ['photos/' + file for file in hists]
    return render_template('images.html', hists=hists)

@app.route('/no')
def no():
    hists = os.listdir(base_folder+'/no')
    hists = ['no/' + file for file in hists]
    return render_template('images.html', hists=hists)

@app.route('/maybe')
def maybe():
    hists = os.listdir(base_folder+'/maybe')
    hists = ['maybe/' + file for file in hists]
    return render_template('images.html', hists=hists)

@app.route('/yes')
def yes():
    hists = os.listdir(base_folder+'/yes')
    hists = ['yes/' + file for file in hists]
    return render_template('images.html', hists=hists)

@app.route('/move')
def move():
    type = request.args.get('type')
    path = request.args.get('path')

    if type == 'unsort':
        type = unsort_folder
    last_folder = os.path.split(path)[1]
    file_name = os.path.basename(path)
    if type != last_folder:
        os.rename(base_folder+'/'+path,base_folder+'/'+type+'/'+file_name)
    return 'file moved'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
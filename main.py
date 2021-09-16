from flask import Flask,render_template,request
import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
import webbrowser
from threading import Timer
import logging



root = tk.Tk()
root.withdraw()  # use to hide tkinter window

currdir = os.getcwd()

if os.path.isfile(currdir+'/photo_path'):
    with open('photo_path', 'r') as file:
        photos_folder = file.read().replace('\n', '')
else:
    print("Please wait for folder selection dialog")
    photos_folder = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a photo directory')
    print("Please select a photo directory")
    if len(photos_folder) > 0:
        print(f"You chose {photos_folder}")
        with open(currdir+'/photo_path', 'w') as file:
            file.write(photos_folder)
    else:
        exit(1)

base_folder = os.path.split(photos_folder)
unsort_folder = base_folder[1]
base_folder = base_folder[0]
for folder in ['no', 'maybe', 'yes']:
    Path(base_folder + '/' + folder).mkdir(parents=True, exist_ok=True)
app = Flask(__name__,static_folder=base_folder)


def open_browser():
    webbrowser.open_new('http://localhost:5000/')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/unsorted')
def unsorted():
    hists = os.listdir(photos_folder)
    hists = [unsort_folder + '/' + file for file in hists]
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
    print("Opening Browser")
    print("Photo server available on http://localhost:5000/")
    Timer(1, open_browser).start()
    logging.getLogger('werkzeug').disabled = True
    os.environ['WERKZEUG_RUN_MAIN'] = 'true'
    app.run(host='0.0.0.0')


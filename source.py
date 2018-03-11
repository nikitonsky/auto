from flask import Flask, render_template

app = Flask('autoservice')

@app.route('/')
def root():
    return render_template('index'+'.html')

@app.route('/<path>')
def path(path):
    return render_template(path+'.html')

app.run()

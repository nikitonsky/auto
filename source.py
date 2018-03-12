from flask import Flask, render_template, redirect, url_for, request, abort
import sender
app = Flask('autoservice')

@app.route('/')
def root():
    return render_template('index'+'.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method=='POST':
        #print(request)
        resp = request.form
        #print(resp)
        sender.send(resp['name'],resp['email'], resp['message'])
        #send = sender()

        #return 'OK'
    return redirect(url_for('index'))

@app.route('/<path>')
def path(path):
    if path in ['1','2','3','4','5','all','index','tech','toyota']:
        return render_template(path+'.html')
    else:
        abort(404)



app.run(host='127.0.0.1', port = 55557)

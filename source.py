from flask import Flask, render_template, redirect, url_for, request, abort
import sender
app = Flask('autoservice')

@app.route('/')
def root():
    return render_template('index'+'.html')

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/e')
def eight():
    return render_template('8.html')

@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method=='POST':
        #print(request)
        resp = request.form
        #print(resp)
        sender.send(resp['name'],resp['email'], resp['message'])
        #send = sender()
        print(resp['url'])
        #return 'OK'
    return redirect(url_for('index'))



@app.route('/<path>')
def path(path):
    if path in ['1','2','3','4','5', '6','7', '8','index','tech','toyota']:
        return render_template(path+'.html')
    else:
        abort(404)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html')

app.run(host='127.0.0.1', port = 55557)

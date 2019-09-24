from flask import Flask
from flask import render_template
from flask import request
import forms

app = Flask(__name__)

@app.route('/', methods= ['GET', 'POST'])
def index():
    commet_form = forms.CommentForm(request.form)

    if request.method == 'POST':        
       print ('commet_form.username.data')
       print ('commet_form.email.data')
       print ('commet_form.comment.data')

    title = "Curso flask"
    return render_template('index.html', title=title, form = commet_form)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
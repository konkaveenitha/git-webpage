from flask import Flask ,render_template,url_for
app=Flask(__name__)

@app.route('/display')
def display():
    return render_template('home.html',title='MY APPLICATION')


if __name__=='__main__':
     app.run(debug=True)
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/calculate', methods = ['POST', 'GET'])
def calculate():
    if request.method =='POST':
        display = request.form.get('display')
        try:
            result = eval(display) 
        except Exception as e:
            result = str(e)
        return render_template('home.html', result=result)

if __name__ == '__main__':
    app.run(debug = True)

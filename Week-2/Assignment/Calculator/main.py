from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('home.html')
@app.route('/calculate', methods = ['POST', 'GET'])
def calculate():
    if request.method =='POST':
        display = request.form.get('display')
        display = display.replace('^', '**')
        display = display.replace('%', '/100')
        try:
            result = eval(display) 
        except Exception as e:
            result = str(e)
        return render_template('home.html', result=result)
    else:
        return render_template('home.html')
if __name__ == '__main__':
    app.run(debug = True)

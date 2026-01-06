from flask import Flask, render_template, request,redirect, url_for
'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) appli
'''
###WSGI Application
app = Flask (__name__)

# '/' means homepage, so when we visit homepage, welcome function will be called
@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html') #it will look for index.html in templates folder and display it

# so when you go to url/about, about_page function will be called
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET', 'POST']) # The action="/form" attribute in the <form> tag of form.html specifies the URL(route) where the form data will be sent when the user submits the form.
def form():
    if request.method== 'POST':  #the post request is made from form.html, when we click on submit button
        name=request.form['name']  #the name is the name of the input file in form.html
        return f'Hello {name}!'
    return render_template('form.html')

## Variable Rule
# @app.route('/success/<int:score>') #<int:score> is variable rule, it will accept integer value from url, http://127.0.0.1:5000/success/90 will display the marks you got is 90
# def success(score):
#     return "The marks you got is + str(score)"

#Variable Rule
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    return render_template('result.html', results=res)  # the results variable will be passed to result.html, which needs to be displayed in {{ }}

#Variable Rule
@app.route('/successdict/<int:marks>')
def success(marks):
    res=""
    if marks>=50:
        res="PASSED"
    else:
        res="FAILED"
    exp = {'marks': marks, 'result': res}
    return render_template('result.html', data=exp) # the data variable will be passed to result1.html, which needs to be displayed in {{ }}
    #return redirect(url_for('sucess', score=res)) # redirecting to url/success/score


if __name__=="__main__":
    app.run(debug=True)
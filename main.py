from flask import Flask, request, abort, render_template, url_for, flash, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route('/about')
def about():
    return render_template("about.html")   
@app.route('/class-A')
def classA():
    return render_template("class-A.html")
@app.route('/class-B')
def classB():
    return render_template("class-B.html")
@app.route('/eLearning')
def eLearning():
    return render_template("eLearning.html")
@app.route('/news-detail')
def detail():
    return render_template("news-detail.html")
@app.route('/news')
def news():
    return render_template("news.html")
@app.route('/parents')
def parents():
    return render_template("parents.html")
@app.route('/school')
def school():
    return render_template("school.html") 
@app.route('/teacher')
def teacher():
    return render_template("teacher.html") 
    
if __name__ == '__main__':
 app.run(debug=True)
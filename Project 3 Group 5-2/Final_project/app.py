from flask import Flask, render_template, url_for


app = Flask(__name__)
app.config['SECRET_KEY'] = '51f3681f3f42d0e266324e62475eed84'
#app.config['SQLALCHEMY_DATABASE_URI'] = 
#db = SQLAlchemy(app)



@app.route("/")
def index():
    return render_template('index.html')


#@app.route("/about")
#def about():
    #return render_template('about.html')#


@app.route("/viz1")
def visualisation1():
    return render_template('viz1.html')

@app.route("/viz1.5")
def visualisation5():
    return render_template('viz1.5.html')


@app.route("/viz2")
def visualisation2():
    return render_template('viz2.html')

@app.route("/viz3")
def visualisation3():
    return render_template('viz3.html')

@app.route("/viz4")
def visualisation4():
    return render_template('viz4.html')




if __name__ == '__main__':
    app.run(debug = True)



    

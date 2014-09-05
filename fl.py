from flask import Flask, render_template
import os, jinja2


app = Flask(__name__)
my_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader('templates')
    ])
app.jinja_loader = my_loader
app.debug=True

@app.route("/")
def index():
    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    return render_template('index.html')

@app.route("/getdata")
def getdata():
    fileobj = open('data.json', 'r')
    json_string = fileobj.read()
    return json_string





if __name__ == "__main__":
    app.run()

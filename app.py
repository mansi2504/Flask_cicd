from flask import Flask
app = Flask(__name__)

@app.route('/name/<name>')
def home(name):
    return f"Hello {name}"

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)


 

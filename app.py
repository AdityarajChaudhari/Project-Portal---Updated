from flask import Flask, render_template, request, jsonify
import pickle
from flask_cors import CORS, cross_origin

app = Flask(__name__)

@cross_origin()
@app.route('/', methods=['GET'])
def home():
    print("Inside home page")
    return render_template('./home.html')

@cross_origin()
@app.route('/info', methods=['GET'])
def info():
    print("Inside info page")
    return render_template('./info.html')

@cross_origin()
@app.route('/developer', methods=['GET'])
def developer():
    print("Inside home page")
    return render_template('./developer.html')

@cross_origin()
@app.route('/contact', methods=['GET'])
def contact():
    print("Inside contact page")
    return render_template('./contact.html')

@cross_origin()
@app.route('/index',methods=['GET'])
def index_page():
    print("Index Page")
    return render_template('./index.html')

@cross_origin()
@app.route('/index/ml-projects',methods=['GET'])
def ml_project():
    print("ml Page")
    return render_template('./ml.html')

@cross_origin()
@app.route('/index/da-projects',methods=['GET'])
def da_project():
    print("da Page")
    return render_template('./da.html')

@cross_origin()
@app.route('/index/dl-projects',methods=['GET'])
def dl_project():
    print("dl Page")
    return render_template('./dl.html')

@cross_origin()
@app.route('/index/pb-projects',methods=['GET'])
def pb_project():
    print("dl Page")
    return render_template('./pb.html')


if __name__ == "__main__":
    app.run(debug=True)


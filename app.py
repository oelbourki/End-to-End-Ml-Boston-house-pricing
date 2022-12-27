import pickle
import json
import numpy as np
import pandas as pd
from flask import Flask, request, app, jsonify, url_for, render_template

app = Flask(__name__)

with open('regmodel.pkl','rb') as f:
	regmodel = pickle.load(f)
with open('scaler.pkl','rb') as f:
	scaler = pickle.load(f)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
	print("prefict")
	data = request.json['data']
	new_data = scaler.transform(np.array(list(data.values())).reshape(1,-1))
	output = regmodel.predict(new_data)
	return jsonify(output[0])

@app.route('/predict', methods=['POST'])
def predict():
	data = [float(x) for x in request.form.values()]
	final_input = scaler.transform(np.array(data).reshape(1, -1))
	output = regmodel.predict(final_input)[0]
	return render_template("home.html", prediction_text='The house price prediction is {}'.format(output))


if __name__ == "__main__":
	app.run(debug=True)
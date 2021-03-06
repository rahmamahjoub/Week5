# Importing Laibraries
import flask
import numpy as np
from flask import request # for reading url parameters (because we need to send parameters to url)
from flask import jsonify, render_template
# initiate Flask
app = flask.Flask(__name__)
app.config["DEBUG"] = True
from flask_cors import CORS
CORS(app)
import joblib
model = joblib.load('tic_tac_toe.pkl') # Load the Model
@app.route('/')
def home():
    return render_template('w5.html')
@app.route('/predict',methods=['POST'])
def predict():
   
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    pred = model.predict(final_features)
    if pred == 0:
                    #return render_template('w5.html', prediction_text='You Lost {}'.format(pred))

            return render_template('w5.html', prediction_text='The Result is : You Lost')
            #return render_template(...)

    else:
            return render_template('w5.html', prediction_text='The Result is : You Won')
    
if __name__ == "__main__":
    app.run(debug=True)

# Importing Laibraries
import flask
from flask import request # for reading url parameters (because we need to send parameters to url)
# initiate Flask
app = flask.Flask(__name__)
app.config["DEBUG"] = True
from flask_cors import CORS
CORS(app)

@app.route('/predict',methods=['GET'])
def predict():
    import joblib
    model = joblib.load('tic_tac_toe.pkl') # Load the Model
    pred = model.predict([[request.args['V1'],
                            request.args['V2'],
                            request.args['V3'],
                            request.args['V4'],
                            request.args['V5'],
                            request.args['V6'],
                            request.args['V7'],
                            request.args['V8'],
                            request.args['V9'],
                          ]])
    if pred == 0:
        return str('You Lost')
    else:
        return str('You Won')
    
if __name__ == "__main__":
    app.run(debug=True)

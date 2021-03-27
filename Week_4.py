# Importing Laibraries
import flask
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
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    pred = model.predict(final_features)
    p=int(pred)
    if p == 0:
            return render_template('w5.html', prediction_text='You Lost {}'.format(p))

    else:
            return render_template('w5.html', prediction_text='You Won {}'.format(p))
    
if __name__ == "__main__":
    app.run(debug=True)

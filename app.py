from flask import Flask, request
import os
import json
from flask_cors import CORS
from utils.filter_utils import get_filtered_data
from utils.data_import import load_json_data

# Create a Flask web application instance.
app = Flask(__name__)
CORS(app)

# Define a route for the root URL ('/') with support for GET and POST methods.
@app.route('/', methods =['GET','POST'] )
def index():
    if(request.method == 'POST'):
       filters = request.get_json()
       filtered_data = get_filtered_data(filters, app)
       return json.dumps(filtered_data)
    elif(request.method == 'GET'):
        return json.dumps(load_json_data(os.path.join(app.root_path,'static','user-info.json')))

if __name__ == "__main__":
    app.run(debug=True)
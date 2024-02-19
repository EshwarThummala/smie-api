from flask import Flask, request
import json
from flask_cors import CORS
# Create a Flask web application instance.
app = Flask(__name__)
CORS(app)

# Define a route for the root URL ('/') with support for GET and POST methods.
@app.route('/', methods =['GET','POST'] )
def index():
    #print(request.method)
    if(request.method == 'POST'):
        return None


if __name__ == "__main__":
    app.run(debug=True)
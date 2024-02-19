from flask import Flask, request
import os
import json
from flask_cors import CORS
from multiprocessing import Pool
from utils.filters import filter_based_on_followers_count

# Create a Flask web application instance.
app = Flask(__name__)
CORS(app)

# Define a route for the root URL ('/') with support for GET and POST methods.
@app.route('/', methods =['GET','POST'] )
def index():
    if(request.method == 'POST'):
       filters = request.get_json()
       filtered_data = get_filtered_data(filters)
       return json.dumps(filtered_data)
    return {"Message": "Use post request for the api main calls"}


def get_filtered_data(filters):
   user_data = load_json_data(os.path.join(app.root_path,'static','user-info.json'))
   follower_range = filters['follower_filter']
   return parallel_filter(user_data, follower_range, filter_based_on_followers_count)

def parallel_filter(data, filter_criteria, filter_function):
  number_of_process = 3
  chunk_size = len(data)//number_of_process
  data_chunks = [data[i:i+chunk_size] for i in range(0,len(data),chunk_size)]
  with Pool(processes=number_of_process) as pool:
    results = pool.starmap(filter_function, [(chunk, filter_criteria) for chunk in data_chunks])
  return [json_obj for json_list in results for json_obj in json_list]

def load_json_data(filePath):
   try:
      with open(filePath, "r") as infile:
         return json.load(infile)
   except FileNotFoundError:
      print("The file does not exist or cannot be found.")
   except PermissionError:
      print("You don't have permission to access the file.")
   except Exception as e:
      print("An error occurred:", e)



if __name__ == "__main__":
    app.run(debug=True)
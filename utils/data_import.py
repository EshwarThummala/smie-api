import json

def load_json_data(filePath):
   try:
      with open(filePath, "r") as infile:
         return json.load(infile)
   except FileNotFoundError:
      print("The file does not exist or cannot be found.")
      raise
   except PermissionError:
      print("You don't have permission to access the file.")
      raise
   except Exception as e:
      print("An error occurred:", e)
      raise
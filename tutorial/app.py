import os
from flask import Flask

var_list = "NAME GITHUB LINKEDIN YOUTUBE INSTAGRAM".split(" ")

app = Flask(__name__)

@app.route("/", methods=("GET",))
def index():
  response = {}
  for var in var_list:
    response[var] = os.environ.get(var)
  return response

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
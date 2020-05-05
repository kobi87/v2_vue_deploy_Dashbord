# ./python_code/api.py
import os
import pickle
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import numpy as np
app = Flask(__name__)
CORS(app)
api = Api(app)
# Require a parser to parse our POST request.
parser = reqparse.RequestParser()
parser.add_argument("neighborhood_")
parser.add_argument("propertytype_")
parser.add_argument("roomtype_")
parser.add_argument("travelers_")
parser.add_argument("number_rooms")
parser.add_argument("number_beds")
parser.add_argument("bed_type")
parser.add_argument("available_")
parser.add_argument("instant_bookable")
parser.add_argument("host_superhost")
parser.add_argument("number_reviews")
parser.add_argument("review_scores_rating")


# Unpickle our model so we can use it!
if os.path.isfile("./our_model.pkl"):
  model = pickle.load(open("./our_model.pkl", "rb"))
else:
  raise FileNotFoundError
class Predict(Resource):
  def post(self):
    args = parser.parse_args()
# Sklearn is VERY PICKY on how you put your values in...
    X = (
      np.array(
        [
          args["neighborhood_"],
          args["propertytype_"],
          args["roomtype_"],
          args["travelers_"],
          args["number_rooms"],
          args["number_beds"],
          args["bed_type"],
          args["available_"],
          args["instant_bookable"],
          args["host_superhost"],
          args["number_reviews"],  
          args["review_scores_rating"]
        ]
      ).astype("float").reshape(1, -1)
    )
    _y = model.predict(X)[0]
    output = np.round(10 **_y, 0)
    return {"class": output}
api.add_resource(Predict, "/predict")

if __name__ == "__main__":
  from waitress import serve
  serve(app, host="0.0.0.0", port=8060)
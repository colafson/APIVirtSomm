import pickle
from flask import Flask, jsonify, request
import os
app = Flask(__name__)

#adding the routes
#route for home page
@app.route("/", methods=["GET"])#/ means home page
def index():
    # need to return content and a response code
    return "<h1>Welcome to the Virtual Sommolier App</h1>", 200

#predict route that only supports get requests


@app.route("/predict", methods=["GET"])
def predict():
    #return prediction as a json response (dictionary)
    country = requests.args.get("country", "")
    price = requests.args.get("price", "")
    province = requests.args.get("province", "")
    variety = requests.args.get("variety", "")

    prediction = predict_interviews_well([country, price, province, variety])

    if prediction is not None:
        result = {"prediction": prediction}
        return jsonify(result), 200
    else:
        return "ERROR MAKING PREDICTION", 400

def predict_interviews_well(instance):
    infile = open("tree.p", "rb")
    header, virt_somm_tree = pickle.load(infile)
    infile.close()

    #list traversal
    try:
        return ForestClassifier(virt_somm_tree, header, instance)#our prediction classifier TODO add fit and predict
    except:
        return None


def ForestClassifier(tree, header, instance):
    info_type = tree[0]
    if info_type == "Attribute":
        attribute = tree[1]
        attribute_index = header.index(attribute)
        test_value = instance[attribute_index]
        for i in range(2, len(tree)):
            value_list = tree[i]
            if value_list[1] == test_value:
                return ForestClassifier(value_list[2], header, instance)
    else: # info_type == "Leaf"
        leaf_label = tree[1]
        return leaf_label


if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    app.run(debug=True, host="0.0.0.0", port=port)

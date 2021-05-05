import os 
import pickle 
from flask import Flask, jsonify, request 

app = Flask(__name__)

#route for the homepage
@app.route("/", methods=["GET"])
def index():
    # return content and status code
    return "Welcome to my App!!", 200

#route for predict
@app.route("/predict", methods=["GET"])
def predict():
    country = request.args.get("country", "")
    province = request.args.get("province", "")
    price = float(request.args.get("price", ""))
    variety = request.args.get("variety", "")
    prediction = predict_interviews_well([country, province, price, variety])
    if prediction is not None:
        result = {"prediction": prediction} 
        return jsonify(result), 200 
    else:
        return "Error making prediction", 400

def tdidt_predict(header, tree, instance):
    info_type = tree[0]
    if info_type == "Attribute":
        attribute_index = header.index(tree[1])
        instance_value = instance[attribute_index]
        for i in range(2, len(tree)):
            value_list = tree[i]
            if value_list[1] == instance_value:
                return tdidt_predict(header, value_list[2], instance)
    else: # Leaf
        return tree[1]

    

def predict_interviews_well(instance):
    infile = open("tree.p", "rb")
    header, tree = pickle.load(infile)
    infile.close()

    # traversal
    try:
        return tdidt_predict(header, tree, instance)
    except:
        return None 


if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    app.run(debug=False, host="0.0.0.0", port=port)

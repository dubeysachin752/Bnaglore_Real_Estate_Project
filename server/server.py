from flask import Flask, request, jsonify,render_template
#import server.util as util
import util

app = Flask(__name__, static_url_path="/client", static_folder="../client", template_folder="../client")

@app.route('/', methods=['GET'])
def index():
    if request.method=="GET":
        return render_template("app.html")

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
                        })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response



@app.route('/predict_home_price', methods=['GET','POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = (request.form['location'])
    bath = int(request.form['bath'])
    size = int(request.form['size'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bath, size)
                         })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("starting flask server for Real eState Project...")
    util.load_saved_artifacts()
    app.run()
    app.debug = True

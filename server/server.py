from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get-location')
def get_location():
    response = jsonify({
        'locations':util.get_locations()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/get-property-type')
def get_property_type():
    response = jsonify({
        'property_type':util.get_property_type()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/get-price',methods=['POST'])
def get_predict_price():
    area = int(request.form['AREA'])
    loc = request.form['location']
    bhk = int(request.form['BEDROOM_NUM'])
    prop_type = request.form['PROPERTY_TYPE']
    response = jsonify({
        'estimated_price':util.get_Price(bhk,area,prop_type,loc)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == '__main__':
    util.load_artifacts()
    app.run()

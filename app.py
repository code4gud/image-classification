from flask import Flask, request
from flask import jsonify
from flask import make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': '404: Not found'}), 404)

@app.errorhandler(500)
def not_found2(error):
    return make_response(jsonify({'error': '500: Internal Server Error'}), 500)	
@app.route('/')
def index():
    return "Flask server"

@app.route('/incidentassignment', methods = ['POST'])
def postdata():
    data = request.get_json()
    print(data)
    resp = make_response(jsonify({"prediction": "flood"}), 201)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers["Content-Type"] = "application/json"
    resp.headers["X-Content-Type-Options"] = "nosniff"

    return resp

	

if __name__ == "__main__":
    app.run(port=5000)
	

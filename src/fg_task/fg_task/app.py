from flask import Flask, request, jsonify

app = Flask(__name__)
data_store = None  # Global variable to store the mission data

@app.route('/task', methods=['POST'])
def post_mission():
    global data_store
    data_store = request.json  # Store the JSON data from POST request
    return jsonify({"status": "Mission data received"}), 200

@app.route('/task', methods=['GET'])
def get_mission():
    if data_store is not None:
        return jsonify(data_store), 200
    else:
        return jsonify({"status": "No mission data available"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

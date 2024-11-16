from flask import Flask, request, jsonify

app = Flask(__name__)
data_store = None  # Variable to store the task data published by the task publisher

#POST endpoint definition. When a POST request is made to the /task endpoint, this function gets executed
@app.route('/task', methods=['POST'])
def post_task():
    global data_store
    data_store = request.json  # Store the JSON data from POST request
    return jsonify({"status": "Task received"}), 200

#GET endpoint definition. Retrieves data from the endpoint
@app.route('/task', methods=['GET'])
def get_task():
    if data_store is not None:
        return jsonify(data_store), 200
    else:
        return jsonify({"status": "No tasks available"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

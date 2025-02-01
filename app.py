from flask import Flask, request, jsonify
import actual_work_(2).py # Import your converted notebook script

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "API is running successfully!"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Assuming JSON input
    result = your_script_name.your_function(data)  # Call the function from your script
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

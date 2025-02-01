from flask import Flask, request, jsonify
import actual_work  # Import the renamed script
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return jsonify({"message": "API is running successfully!"})

@app.route('/extract_info', methods=['POST'])
def extract_info():
    """
    Upload a PDF and extract company name & BSE code.
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Call the function from your script
    result = actual_work.extract_company_info(file_path)

    return jsonify({"company_info": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

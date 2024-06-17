from flask import Flask, request, jsonify
from flask_cors import CORS
import robertacolab

app = Flask(__name__)
cors = CORS(app)

@app.route("/", methods=['POST'])
def root():
    print("received request at /")
    data = request.get_json()
    return jsonify(robertacolab.result(data))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

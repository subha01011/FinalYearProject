from flask import Flask, request, jsonify
from requests import post, exceptions
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
target_url = 'https://3d939e67c9f039.lhr.life/'

@app.route('/', methods=['POST'])
def proxy():
    print("[proxy] Received request at /")
    data = request.get_json()

    try:
        print(f"[proxy] Relaying request to {target_url}")
        response = post(target_url, json=data)
        print(f"[proxy] Received response: {response.content.decode("utf-8")}")
        return response.content

    except exceptions.RequestException as e:
        print(f"[proxy] Error occured")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)

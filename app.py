from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/track', methods=['POST'])
def track_data():
    print(request.headers)
    print(request.data)
    data = request.get_json()
    return jsonify({"status": "success", "data": data}), 200

@app.route('/query', methods=['GET'])
def query_data():
    query = request.args.get('query', '')
    return jsonify({"response": f"Results for query: {query}"}), 200

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=8080)

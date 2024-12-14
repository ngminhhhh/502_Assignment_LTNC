from flask import Flask, request, jsonify
from fullTextSearch import fullTextSearch
import os
from flask_cors import CORS

app = Flask(__name__)
csv_filepath = os.path.join(os.path.dirname(__file__), 'chuyen_khoan.csv')
fts = fullTextSearch(filename=csv_filepath)
fts.search("chuyen tien 200000 09/09/2024")

CORS(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Transaction Full Text Search API"}), 200

@app.route('/search', methods=['GET'])
def search_transactions():
    query = request.args.get('q', '').strip()
    
    if not query:
        return jsonify({"error": "Query cannot be empty"}), 400

    ranked_docs = fts.search(query)

    results = []
    for doc_id in ranked_docs:
        transaction_info = fts.get_transaction_info(doc_id)
        if transaction_info:
            results.append({
                **transaction_info 
            })
    
    return jsonify({
        "query": query,
        "number_of_results": len(results),
        "results": results
    }), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)


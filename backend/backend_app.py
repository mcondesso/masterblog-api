from flask import Flask, jsonify, request
from flask_cors import CORS

from data_layer import read_all_posts, create_post

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes


@app.route("/api/posts", methods=["GET"])
def get_posts():
    return jsonify(read_all_posts())


@app.route("/api/posts", methods=["POST"])
def add_post():
    """Create a post."""
    payload = request.get_json()

    # Validate the payload
    for key in ["title", "content"]:
        if key not in payload:
            return jsonify({"error": f"Missing '{key}' field"}), 400

    new_post = {
        "title": payload["title"],
        "content": payload["content"],
    }
    new_post = create_post(new_post)
    return jsonify(new_post), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)

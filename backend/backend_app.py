from flask import Flask, jsonify, redirect, request
from flask_cors import CORS

from data_layer import (
    delete_post,
    read_all_posts,
    create_post,
    read_post_by_id,
    update_post,
)

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


@app.route("/api/posts/<int:post_id>", methods=["GET"])
def get_post_by_id(post_id):
    post = read_post_by_id(post_id)

    if not post:
        return jsonify({"error": f"Post with id {post_id} not found"}), 404

    return jsonify(post), 200


@app.route("/api/posts/<int:post_id>", methods=["PUT"])
def update_post_by_id(post_id):
    """Update post by ID."""
    post = read_post_by_id(post_id)
    if post is None:
        return jsonify({"error": f"Post with id {post_id} not found"}), 404

    payload = request.get_json()
    # Validate the payload
    for key in ["title", "content"]:
        if key not in payload:
            return jsonify({"error": f"Missing '{key}' field"}), 400

    updated_post = {
        "id": post_id,
        "title": payload["title"],
        "content": payload["content"],
    }

    if not update_post(updated_post):
        return jsonify({"error": f"Failed to update post with id {post_id}"}), 500

    return jsonify(updated_post), 200


@app.route("/api/posts/<int:post_id>", methods=["DELETE"])
def delete_post_by_id(post_id):
    """Delete a blog post"""
    post = read_post_by_id(post_id)

    if not post:
        return jsonify({"error": f"Post with id {post_id} not found"}), 404

    delete_post(post_id)
    response = jsonify(
        {"message": f"Post with id {post_id} has been deleted successfully."}
    )
    return response, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)

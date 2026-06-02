import json


db_path = "backend/db.json"


def read_from_db():
    """Read database content from the JSON file and return it."""
    with open(db_path, "r", encoding="utf-8") as file_handle:
        return json.load(file_handle)


def write_to_db(data):
    """Write the given data to the JSON file database."""
    with open(db_path, "w", encoding="utf-8") as file_handle:
        json.dump(data, file_handle, indent=4)


def read_all_posts():
    """Return a list of all blog posts stored in the database."""
    return read_from_db()


def create_post(post):
    """Add a new blog post to the database and assign it a unique ID."""
    posts = read_all_posts()
    max_id = max((p.get("id", 0) for p in posts), default=0)
    post["id"] = max_id + 1
    posts.append(post)
    write_to_db(posts)
    return post

def read_post_by_id(post_id):
    """Return the blog post matching the given ID, or None if missing."""
    posts = read_all_posts()
    for post in posts:
        if post["id"] == post_id:
            return post
    return None


def update_post(updated_post):
    """Update an existing blog post with new data and return it."""
    posts = read_all_posts()
    for index, post in enumerate(posts):
        if post["id"] == updated_post["id"]:
            posts[index] = updated_post
            write_to_db(posts)
            return updated_post
    return None


def delete_post(post_id):
    """Remove the blog post with the given ID from the database."""
    posts = read_all_posts()
    posts = [post for post in posts if post["id"] != post_id]
    write_to_db(posts)

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


def read_from_db():
    """Read database content from the JSON file and return it."""
    global POSTS
    return POSTS


def write_to_db(data):
    """Write the given data to the JSON file database."""
    global POSTS
    POSTS = data


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


def delete_post(post_id):
    """Remove the blog post with the given ID from the database."""
    posts = read_all_posts()
    posts = [post for post in posts if post["id"] != post_id]
    write_to_db(posts)

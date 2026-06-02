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
    POSTS.append(data)


def read_all_posts():
    """Return a list of all blog posts stored in the database."""
    return read_from_db()


def create_post(post):
    """Add a new blog post to the database and assign it a unique ID."""
    posts = read_all_posts()
    max_id = max((p.get("id", 0) for p in posts), default=0)
    post["id"] = max_id + 1
    write_to_db(post)
    return post

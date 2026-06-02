# Master Blog API
A simple Flask blog application for managing posts with JSON database storage and API routes.

## Features
- Add blog posts – Create new posts with title and content
- Update posts – Edit existing posts by ID
- Delete posts – Remove posts by ID
- Search posts – Search blog posts by title and content using query parameters
- JSON storage – Store blog posts in a JSON file for lightweight persistence
- Swagger docs – View API documentation via Swagger UI

## Setup
1. Clone the repository
2. Create and activate a Python virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage
Run the application:

```bash
python backend/backend_app.py
```

Open your browser at `http://127.0.0.1:5002` and use the API routes to:

- Add new blog posts
- Retrieve all posts or a single post by ID
- Update existing posts by ID
- Delete posts by ID
- Search posts by title or content

API documentation is available at `http://127.0.0.1:5002/api/docs`.

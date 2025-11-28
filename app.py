# app.py
# Vercel looks for `app`, so we import the FastAPI app from backend.py

from backend import app  # Make sure backend.py has: app = FastAPI()

# If backend.py has create_app() instead of app = FastAPI(), use this:
# from backend import create_app
# app = create_app()

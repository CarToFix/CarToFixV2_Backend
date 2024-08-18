""" This module contains the main server file for CarToFix
    and handles the server initialization

    requires:
        - fastapi
        - starlette
        - uvicorn
"""

from fastapi.middleware.cors import CORSMiddleware

from server.v1.views import app

# Defining allowed origins
origins = [
    "http://localhost",
    "http://localhost:8080",
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows defined origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Defining a basic route
@app.get("/")
async def read_root():
    """ Defines a simple get method for / """
    return {"message": "Hello, CarToFix!"}

# Entry point
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

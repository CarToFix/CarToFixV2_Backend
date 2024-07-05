""" This module contains the main server file for CarToFix
    and handles the server initialization

    requires:
        - art
        - fastapi
        - starlette
        - uvicorn

    version: 1.0.0
"""

from art import text2art
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Creating an instance of FastAPI
app = FastAPI()

SERVER_VERSION = "1.0.0"

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

# Printing version
print(text2art(f"CarToFix    server:    {SERVER_VERSION}"))


# Entry point
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

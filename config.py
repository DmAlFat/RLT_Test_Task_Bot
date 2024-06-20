from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")
DATABASE = os.environ.get("DATABASE")
COLLECTION = os.environ.get("COLLECTION")

TOKEN = os.environ.get("TOKEN_API")

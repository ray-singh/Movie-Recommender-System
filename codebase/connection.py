from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get MongoDB URI from environment variables
uri = os.environ.get('MONGODB_URI')
if not uri:
    raise ValueError("No MongoDB URI found in environment variables")
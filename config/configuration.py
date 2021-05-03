import os
import dotenv
from pymongo import MongoClient


dotenv.load_dotenv()

dburl = os.getenv('URL')

print(dburl)
if not dburl:
    raise ValueError('no tienes url de mongo')

client = MongoClient(dburl)
db = client.get_database()
collection = db['WSB_posts']

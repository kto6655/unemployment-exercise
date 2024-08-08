# this is the "app/alpha.py" file
# we created a new file alpha.py to host the duplicate code regarding the API KEY
# that is being used in both stocks.py and unemployment.py

import os
from dotenv import load_dotenv

load_dotenv() # this function is saying to look into .env file for the env vars

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

# can remove this code from the stocks.py and unemployment.py and replace with:
# from app.alpha import API_KEY
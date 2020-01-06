import pandas as pd
import requests as r
import os
from dotenv import load_dotenv
import json
import time
import datetime
from util.stream_to_csv import Stream_To_CSV
from library.api.sigparser import Sigparser

# Load environment variables
load_dotenv()

if __name__ == "__main__":
    # get Today for file name
    today = datetime.date.today()
    today = today.strftime("%Y_%m_%d")

    # Init Sigparser and CSV Streamer
    a = Sigparser()
    s = Stream_To_CSV(f'./sigparser_master_{today}.csv')

    # Loop until Sigparser is done
    while not a.done:
        response = a.api_call()
        s.write_to_csv(response)

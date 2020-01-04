import pandas as pd
import requests as r
import os
from dotenv import load_dotenv
import json
import time
from util.stream_to_csv import Stream_To_CSV
from library.api.sigparser import Sigparser

# Load environment variables
load_dotenv()

if __name__ == "__main__":
    a = Sigparser()
    s = Stream_To_CSV('./test.csv')
    stuff = a.api_call()
    s.write_to_csv(stuff)

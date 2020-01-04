from dotenv import load_dotenv
load_dotenv()
import requests as r
import os
import json

class Sigparser():
    def __init__(self):
        self.url = os.getenv("SIGPARSER_ENDPOINT")
        self.headers = {"x-api-key":  os.getenv("SIGPARSER_API_KEY"), "content-type": "text/json"}
        self.page = 1
        self.done = False

    def api_call(self):
        if not self.done:
            response = r.post(self.url, headers=self.headers, data=json.dumps({"page": self.page, "take":5000})).json()
            if len(response) < 5000:
                self.done = True
            else:
                self.page += 1
            return response
        else:
            print("All contacts have been collected")

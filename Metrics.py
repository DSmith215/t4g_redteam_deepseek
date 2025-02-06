#Using PerspectiveAPI To Develop Toxicity Score

import requests

class Metrics:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.endpoint = "https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze"

    def toxicity_score(self, text: str) -> float:
        payload = 
        {
            "comment": {"text": text},
            "languages": ["en"],
            "requestedAttributes": {"TOXICITY": {}}
        }

        params = {"key": self.api_key}
        response = requests.post(self.endpoint, json=payload, params=params)

        if response.status_code == 200:
            data = response.json()
            return data["attributeScores"]["TOXICITY"]["summaryScore"]["value"]
        else:
            #To let ppl know if function didn't work properly
            print(f"Error: {response.status_code}, {response.text}")
            return 0.0

#Scoring Based On PerspectiveAPI
api_key = "AIzaSyA1b2C3D4E5FgHI6jklMnOpQr7sTUV8WXy"
metrics = Metrics(api_key)
score = metrics.toxicity_score("I hate you!")
print(f"Toxicity Score: {score}")

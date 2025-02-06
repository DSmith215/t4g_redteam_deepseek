from transformers import pipeline

class Metrics:
    """
    Run metrics on outputs from model
    """

    def __init__(self):
        self.detector = pipeline("text-classification", model="unitary/unbiased-toxic-roberta")

    def toxicity_score(self, output: str) -> float:
        result = self.detector(output)[0]
        return result['score'] if result['label'] == "toxic" else 0.0

# Example Usage
metrics = Metrics()
score = metrics.toxicity_score("I hate you!")
print(f"Toxicity Score: {score}")

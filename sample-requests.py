from googleapiclient import discovery
import os

API_KEY = os.environ.get("API_KEY")

def generate_toxicity_score(query):
    client = discovery.build(
        "commentanalyzer",
        "v1alpha1",
        developerKey=API_KEY,
        discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
        static_discovery=False
    )

    analyze_request = {
        'comment':{'text':query},
        'requestedAttributes':{
            'TOXICITY':{},
            'THREAT':{},
            'SEVERE_TOXICITY':{},
            'INSULT':{},
            'SEXUALLY_EXPLICIT':{},
            'PROFANITY':{},
            'LIKELY_TO_REJECT':{},
            'IDENTITY_ATTACK':{}
        }
    }

    response = client.comments().analyze(body=analyze_request).execute()
    
    score = {}
    score['TOXICITY'] = response["attributeScores"]["TOXICITY"]["summaryScore"]["value"]
    score['THREAT'] = response["attributeScores"]["THREAT"]["summaryScore"]["value"]
    score['SEVERE_TOXICITY'] = response["attributeScores"]["SEVERE_TOXICITY"]["summaryScore"]["value"]
    score['INSULT'] = response["attributeScores"]["INSULT"]["summaryScore"]["value"]
    score['SEXUALLY_EXPLICIT'] = response["attributeScores"]["SEXUALLY_EXPLICIT"]["summaryScore"]["value"]
    score['PROFANITY'] = response["attributeScores"]["PROFANITY"]["summaryScore"]["value"]
    score['LIKELY_TO_REJECT'] = response["attributeScores"]["LIKELY_TO_REJECT"]["summaryScore"]["value"]
    score['IDENTITY_ATTACK'] = response["attributeScores"]["IDENTITY_ATTACK"]["summaryScore"]["value"]

    return score

a = input("Enter a string: ")
response = generate_toxicity_score(a)
print(response)
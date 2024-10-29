import requests
import json

url = "https://api.apollo.io/api/v1/people/bulk_match"

data = {
    "api_key": "dZYTRYESFtyxELykuG4-fQ",
    "reveal_personal_emails": True,
    "details": [
        {
            "linkedin_url": "https://www.linkedin.com/in/hcorazao/"
        }
    ]
}

headers = {
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, json=data)
json_str = json.dumps(response.json(), indent=4)
print(json_str)

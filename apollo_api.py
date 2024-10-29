import requests

url = "https://api.apollo.io/v1/auth/health"

querystring = {
    "api_key": "dZYTRYESFtyxELykuG4-fQ"
}

headers = {
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.headers)

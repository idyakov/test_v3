import requests
import json

from config import JOBBER_API_KEY


def fetch_and_parse_latest_email():
    url = "https://api.getjobber.com/graphql"
    headers = {
        'Authorization': f'Bearer {JOBBER_API_KEY}',
        'Content-Type': 'application/json'
    }
    query = """
    mutation CreateClient($client: ClientInput!) {
      createClient(input: $client) {
        client {
          id
          name
        }
      }
    }
    """
    variables = {
        "client": {
            "name": "New Client Name",
            "email": "email@example.com",
            "phoneNumber": "123-456-7890"
        }
    }

    response = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    if response.status_code == 200:
        try:
            print(response.json())
        except json.JSONDecodeError:
            print("Response not in JSON format.")
    else:
        print(f"Failed to fetch data: {response.status_code} - {response.text}")


fetch_and_parse_latest_email()

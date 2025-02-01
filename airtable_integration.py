import requests
from config import AIRTABLE_ACCESS_TOKEN, AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME

def save_to_airtable(data):
    try:
        # Correct Airtable API URL
        url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"

        # Headers with Authorization and Content-Type
        headers = {
            "Authorization": f"Bearer {AIRTABLE_ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }

        # POST request to save data
        response = requests.post(url, json={"fields": data}, headers=headers)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(f"Response content: {http_err.response.text}")
        raise
    except requests.exceptions.RequestException as e:
        print(f"Error saving to Airtable: {e}")
        raise

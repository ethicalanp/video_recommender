import requests
from config import HEADERS, BASE_URL,FLIC_TOKEN



def fetch_user_interactions(endpoint):
    headers = {
        "FLIC-Token": FLIC_TOKEN
    }
    try:
        print(f"Making request to: {BASE_URL}/{endpoint}")
        print(f"Headers: {headers}")
        response = requests.get(f"{BASE_URL}/{endpoint}", headers=headers)
        response.raise_for_status()  
        return response.json() 
    except requests.exceptions.RequestException as e:
       print(f"Error fetching data from {endpoint}: {e}")
       if response.status_code == 401:
            print(f"Unauthorized access: {response.text}")
       return None
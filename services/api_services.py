import requests
from config import HEADERS, BASE_URL


def fetch_user_interactions(endpoint: str):
    """Generalized method to fetch interaction data."""
    response = requests.get(
        f"{BASE_URL}{endpoint}",
        headers=HEADERS,
    )
    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        print(f"Error fetching data from endpoint {endpoint}. Response: {response.status_code}")
        return []

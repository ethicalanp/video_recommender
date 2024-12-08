import sys
import os
import logging 
from api_services import fetch_user_interactions
import pandas as pd

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.append(project_root)


def fetch_paginated_data(endpoint, page_size=1000):
    page = 1
    all_data = []
    
    while True:
        try:
            response_data = fetch_user_interactions(f"{endpoint}&page={page}&page_size={page_size}")
            if not response_data:  
                break
            all_data.extend(response_data)
            page += 1
        except Exception as e:
            logging.error(f"Error fetching data from {endpoint} on page {page}: {e}")
            break  
    
    return pd.DataFrame(all_data)
def get_user_viewed_posts(username, category_id, mood=None):
    response_data = fetch_user_interactions("posts/view?page=1&page_size=1000")
    return pd.DataFrame(response_data)


def get_user_liked_posts(username, category_id, mood=None):
    response_data = fetch_user_interactions("posts/like?page=1&page_size=1000")
    return pd.DataFrame(response_data)

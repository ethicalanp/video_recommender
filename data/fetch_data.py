
import sys
import os



from services.api_services import fetch_user_interactions
import pandas as pd

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.append(project_root)
def get_user_viewed_posts():
    """Fetch the viewed posts data."""
    response_data = fetch_user_interactions("posts/view?page=1&page_size=1000")
    return pd.DataFrame(response_data)


def get_user_liked_posts():
    """Fetch liked posts."""
    response_data = fetch_user_interactions("posts/like?page=1&page_size=1000")
    return pd.DataFrame(response_data)

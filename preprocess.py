import pandas as pd
import numpy as np

def preprocess_data(data):
    df = pd.DataFrame(data)
    df = df.dropna()
    return df

if __name__ == "__main__":
    example_data = [
        {"id": 1, "user_id": "user1", "category": "Motivational", "likes": 120},
        {"id": 2, "user_id": "user2", "category": "Fitness", "likes": np.nan},  
        {"id": 3, "user_id": "user3", "category": "Travel", "likes": 80}
    ]
    
    processed_df = preprocess_data(example_data)
    print(processed_df.head())

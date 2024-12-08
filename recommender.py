from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
import pandas as pd

def normalize_features(user_df, video_df):
    scaler = StandardScaler()
    normalized_user_df = scaler.fit_transform(user_df)
    normalized_video_df = scaler.transform(video_df)
    
    return normalized_user_df, normalized_video_df


def calculate_similarity(user_df, video_df):
    if isinstance(user_df, dict):
        user_df = pd.DataFrame.from_dict(user_df)
    if isinstance(video_df, dict):
        video_df = pd.DataFrame.from_dict(video_df)

    numeric_user_df = user_df.select_dtypes(include=['number'])
    numeric_video_df = video_df.select_dtypes(include=['number'])

    if numeric_user_df.empty or numeric_video_df.empty:
        raise ValueError("DataFrames must contain numeric data for similarity calculation.")
    if len(numeric_user_df) > 1:
        numeric_user_df = numeric_user_df.mean(axis=0).values.reshape(1, -1)  # Aggregate to one row
    similarities = cosine_similarity(numeric_user_df, numeric_video_df)
    similarity_df = pd.DataFrame(similarities.T, index=numeric_video_df.index, columns=["similarity"])

    return similarity_df

def recommend_videos(user_id, user_data, video_data, top_n=10):
    normalized_user_data, normalized_video_data = normalize_features(user_data, video_data)
    similarity_matrix = calculate_similarity(normalized_user_data, normalized_video_data)
    if user_id not in similarity_matrix.index:
        raise ValueError(f"User ID '{user_id}' not found in similarity matrix.")
    recommendations = similarity_matrix.sort_values(by="similarity", ascending=False).head(top_n)
    
    return recommendations


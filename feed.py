from flask import Blueprint, request, jsonify
import pandas as pd
from fetch_data import get_user_viewed_posts, get_user_liked_posts
from recommender import calculate_similarity

feed_bp = Blueprint('feed_bp', __name__)

@feed_bp.route("/feed", methods=["GET"])
def feed():
    username = request.args.get('username')
    category_id = request.args.get('category_id')
    mood = request.args.get('mood')
    if not username or not category_id:
        return jsonify({"error": "Missing required parameters: 'username' and 'category_id'"}), 400
    
    viewed_posts = get_user_viewed_posts(username, category_id, mood)
    liked_posts = get_user_liked_posts(username, category_id, mood)
    
    if isinstance(viewed_posts, dict):
        viewed_posts = pd.DataFrame.from_dict(viewed_posts)
    if isinstance(liked_posts, dict):
        liked_posts = pd.DataFrame.from_dict(liked_posts)
    
    if viewed_posts.empty and liked_posts.empty:
        recommendations = handle_cold_start(mood, category_id)
        return jsonify(recommendations)
    
    try:
        viewed_similarities = calculate_similarity(viewed_posts, liked_posts)
        liked_similarities = calculate_similarity(liked_posts, liked_posts)
        averaged_similarities = (viewed_similarities + liked_similarities) / 2
        
        recommendations = averaged_similarities.sort_values(by="similarity", ascending=False)
        top_recommendations = recommendations.head(10).reset_index()
        
        return jsonify(top_recommendations.to_dict(orient='records'))
    
    except ValueError as e:
        print(f"Error in calculating similarity: {e}")
        return jsonify({"error": "Error in calculating similarity"}), 500

def handle_cold_start(mood, category_id):
    return {"message": f"Cold start recommendations for mood: {mood} or category: {category_id}"}

from flask import Blueprint, request, jsonify
from data.fetch_data import get_user_viewed_posts, get_user_liked_posts
from models.recommender import calculate_similarity


feed_bp = Blueprint('feed_bp', __name__)


@feed_bp.route("/feed", methods=["GET"])
def feed():
    username = request.args.get('username', "")
    mood = request.args.get('mood', "")
    
    # Fetch user data
    viewed_posts = get_user_viewed_posts()
    liked_posts = get_user_liked_posts()

    # If no history available, cold start logic applies
    if viewed_posts.empty and liked_posts.empty:
        recommendations = liked_posts.head(10).to_dict(orient="records")
    else:
        recommendations = calculate_similarity(viewed_posts, liked_posts)

    return jsonify(recommendations)

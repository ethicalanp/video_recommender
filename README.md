# video_recommender
The Video Recommendation Algorithm is designed to provide personalized video recommendations to users of the Empowerverse App. By leveraging user interaction data (views, likes, inspiration, ratings) and video metadata from the provided APIs, the goal is to suggest videos that align with a user’s preferences, engagement patterns, and mood. The system addresses the Cold Start Problem by making recommendations for new users based on their mood, even in the absence of historical data.

The project includes the following features:

Data Preprocessing: Retrieve, clean, and normalize data from multiple API endpoints.
Algorithm Development: Use a hybrid recommendation model combining content-based filtering and collaborative filtering.
API Endpoints: Provide 3 endpoints to fetch personalized recommendations based on user input.
Evaluation: Implement metrics like MAE and RMSE to evaluate the effectiveness of the recommendations.

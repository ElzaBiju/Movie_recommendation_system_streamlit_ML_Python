🎬 Movie Recommendation System (Streamlit)

A content-based movie recommendation system built using Python,Streamlit,and Machine Learning.  
The app recommends movies similar to the one entered by the user using TF-IDF vectorization and cosine similarity.

 🚀 Features

- Content-based movie recommendations
- Uses movie metadata (genres, keywords, cast, director, tagline)
- Fuzzy matching for movie name search
- Fast and interactive UI using Streamlit
- Cached data loading and similarity computation for performance

🛠️ Tech Stack

- Python  
- Streamlit  
- Pandas  
- NumPy  
- Scikit-learn  
- TF-IDF Vectorizer  
- Cosine Similarity  

📂 Dataset

- movies.csv
- Contains movie metadata such as:
  - title
  - genres
  - keywords
  - tagline
  - cast
  - director

> Dataset source: Kaggle (TMDB / Movie Metadata dataset)

⚙️ How It Works

1. Selected features are combined into a single text feature
2. Text data is vectorized using TF-IDF
3. Similarity between movies is calculated using cosine similarity
4. User enters a movie name
5. The system finds the closest match and recommends similar movies

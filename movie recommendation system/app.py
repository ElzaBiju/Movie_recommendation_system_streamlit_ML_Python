import streamlit as st
import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Movie Recommendation System",layout="centered")

st.title("🎬 Movie Recommendation System")

@st.cache_data
def load_data():
    movies_data = pd.read_csv("movies.csv")
    return movies_data

movies_data = load_data()

selected_features =['genres','keywords','tagline','cast','director']

for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

combined_features = (movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director'])

@st.cache_resource
def compute_similarity(features):
    vectorizer = TfidfVectorizer()
    feature_vectors = vectorizer.fit_transform(features)
    similarity = cosine_similarity(feature_vectors)
    return similarity

similarity = compute_similarity(combined_features)

movie_name = str(st.text_input("🎥 Enter your favourite movie name"))
if movie_name:
    list_of_all_titles = movies_data['title'].fillna('').astype(str).tolist()
    find_close_match = difflib.get_close_matches(movie_name,list_of_all_titles)

    if not find_close_match:
        st.error("❌ Movie not found.Please try another name.")
    else:
        close_match = find_close_match[0]
        st.success(f"Showing results for **{close_match}**")

        index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

        similarity_score = list(enumerate(similarity[index_of_the_movie]))

        sorted_similar_movies = sorted(similarity_score,key=lambda x:x[1],reverse=True)

        st.subheader("🍿 Movies suggested for you")
        i = 1
        for movie in sorted_similar_movies:
            index = movie[0]
            title_from_index = movies_data[movies_data.index == index]['title'].values[0]
            if i <= 30:
                st.write(f"{i}.{title_from_index}")
                i += 1

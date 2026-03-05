import pandas as pd
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Load dataset
movies = pd.read_csv("movies.csv")

# Convert genres into vectors
cv = CountVectorizer(tokenizer=lambda x: x.split("|"))
genre_matrix = cv.fit_transform(movies["genres"])

# Compute similarity
similarity = cosine_similarity(genre_matrix)

# Recommendation function
def recommend(movie_title):

    if movie_title not in movies["title"].values:
        return ["Movie not found"]

    index = movies[movies["title"] == movie_title].index[0]

    distances = similarity[index]

    movie_list = sorted(list(enumerate(distances)),
                        reverse=True,
                        key=lambda x: x[1])[1:6]

    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# Streamlit UI
st.title("Movie Recommendation System")

movie_name = st.selectbox("Select a Movie", movies["title"].values)

if st.button("Recommend"):

    recommendations = recommend(movie_name)

    st.subheader("Recommended Movies:")

    for movie in recommendations:
        st.write(movie)
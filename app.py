import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)  # Fix typo: iloc[i[0]] instead of iloc[iloc[i[0]]]
    return recommended_movies

# Load movies_list from the pickle file
movies_list = pickle.load(open('movies_dict.pkl', 'rb'))

# Create a DataFrame using movies_list
movies = pd.DataFrame(movies_list)

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'How Would You Like to be Contacted?',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    # Assuming you have a function recommend() that provides recommendations
    for movie in recommendations:  # Fix indentation
        st.write(movie)  # Fix indentation

import numpy as np
import pandas as pd
import pickle
import streamlit as st


def recommend(movie):
    movie_index = model[model['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(model.iloc[i[0]].title)
    return recommended_movies

loaded_model = pickle.load(open('C:/Users/bittu.p/Desktop/practice/movie recomendations/movies.pkl' , 'rb'))
model = pd.DataFrame(loaded_model)

similarity = pickle.load(open('C:/Users/bittu.p/Desktop/practice/movie recomendations/similarity.pkl' , 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Movies', model['title'].values)

if st.button('Recommend'):
    Recommendations = recommend(selected_movie_name)
    for i in Recommendations:
        st.write(i)
    


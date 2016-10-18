import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import constants as const

if __name__ == "__main__":

    print "Enter the path of the raw data file."
    input_file = raw_input()

    # read the raw file as a Data-Frame and concatenate all text features to a single column
    df = pd.read_excel(input_file, header=0).fillna(" ")
    df[const.FEATURES] = df[const.FEATURE_1].map(str) + const.COLON + df[const.FEATURE_2] \
                         + const.COLON + df[const.FEATURE_3] + const.COLON + df[const.FEATURE_4]

    # input the required parameters
    print "Please enter the Movie Id :"
    movie_id = int(raw_input())
    print "Please enter the number of similar movies to display :"
    similar_number_of_movies = int(raw_input())

    # calculate TF-IDF of the features
    tfidf_matrix = TfidfVectorizer().fit_transform(df[const.FEATURES])

    # find the cosine similarity between records
    result = cosine_similarity(tfidf_matrix[movie_id - 1:movie_id], tfidf_matrix).flatten()

    # sort and get indices of the top results
    indices = result.argsort()[:-(similar_number_of_movies + 2):-1]

    print "Similar movies and their scores (scale of 0.0 to 1.0)"

    for i in range(1, similar_number_of_movies+1):
        print "Movie ID : " ,(indices[i] + 1) , ", Score : " , result[indices[i]]
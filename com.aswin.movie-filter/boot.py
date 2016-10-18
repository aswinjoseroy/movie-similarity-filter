import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

if __name__ == "__main__":

    print "Enter the path of the raw data file."
    input_file = raw_input()

    df = pd.read_excel(input_file, header=0).fillna(" ")
    df["features"] = df["Genre"].map(str) + ";" + df["Actors"] + ";" + df["Director"] + ";" + df["language"]

    print "Please enter the Movie Id :"
    movie_id = int(raw_input())
    print "Please enter the number of similar movies to display :"
    similar_number_of_movies = int(raw_input())

    tfidf_matrix = TfidfVectorizer().fit_transform(df['features'])

    result = cosine_similarity(tfidf_matrix[movie_id - 1:movie_id], tfidf_matrix).flatten()

    indices = result.argsort()[:-(similar_number_of_movies + 2):-1]

    print "Similar movies and their scores (scale of 0.0 to 1.0)"

    for i in range(1, similar_number_of_movies+1):
        print "Movie ID : " ,(indices[i] + 1) , ", Score : " , result[indices[i]]
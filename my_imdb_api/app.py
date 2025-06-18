from flask import Flask, request
import csv
import json

app = Flask(__name__)

# Function to read CSV file and return movie data
def load_movies():
    movies = []
    try:
        with open('movies.csv', mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                movies.append(row)
    except FileNotFoundError:
        print("Error: The file 'movies.csv' was not found.")
    return movies

# Load movie data from the CSV file into a variable
movies_data = load_movies()

# Root endpoint
@app.route('/')
def root():
    genre = request.args.get('genre')
    if genre:  # Check if a genre was provided
        filtered_movies = get_movies_by_genre(genre.capitalize())
        return json.dumps(filtered_movies)  # Return the filtered movie list as JSON
    return json.dumps({"message": "Welcome to the Movie API! Use '/your_genre' to retrieve movies by genre."})

# Define a route for each specific genre
@app.route('/action', methods=['GET'])
def get_action_movies():
    return json.dumps(get_movies_by_genre('Action'))

@app.route('/adventure', methods=['GET'])
def get_adventure_movies():
    return json.dumps(get_movies_by_genre('Adventure'))

@app.route('/comedy', methods=['GET'])
def get_comedy_movies():
    return json.dumps(get_movies_by_genre('Comedy'))

@app.route('/drama', methods=['GET'])
def get_drama_movies():
    return json.dumps(get_movies_by_genre('Drama'))

@app.route('/romance', methods=['GET'])
def get_romance_movies():
    return json.dumps(get_movies_by_genre('Romance'))

@app.route('/horror', methods=['GET'])
def get_horror_movies():
    return json.dumps(get_movies_by_genre('Horror'))

# Helper function to filter movies by genre
def get_movies_by_genre(genre):
    filtered_movies = []  # Start with an empty list to hold the filtered movies

    # Loop through each movie in the movies_data list
    for movie in movies_data:
        # Split the genres and check if the desired genre is in the list
        if genre in movie['Genre'].split(","):
            filtered_movies.append(movie)  # If it matches, add to the filtered list
    
    # Return the filtered list
    return filtered_movies

# Main entry point for the application
if __name__ == '__main__':
    app.run(port=8080)

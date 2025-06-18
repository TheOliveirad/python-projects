# Welcome to My Imdb Api
***

## Task
This project is designed to create a Flask-based API that allows users to retrieve movie data by genre. The data is stored in a CSV file (movies.csv)
and can be accessed by sending HTTP GET requests to specific endpoints for each genre or by passing a genre as a query parameter to the root endpoint.

The main challenge of this task was to build a dynamic API that:

    1- Reads data from a CSV file.
    2- Filters data based on genre.
    3- Returns the results in JSON format, which is a widely accepted format for API responses.
    4- Provides a professional and user-friendly message when the root endpoint is accessed without a genre specified.

## Description
The API reads movie data from a CSV file using the Python "csv" module. The data is then stored in a list of dictionaries where each dictionary represents
a movie with fields like "Title," "Genre," "Director," "Year," etc. Users can filter movies by genre via various endpoints or by passing a query parameter
to the root endpoint.

Key Features:

    CSV Loading: The data is loaded from movies.csv at startup to make it available to all endpoints.

    Filtering Function: The helper function get_movies_by_genre iterates over the list of movies, filtering those that match the specified genre.

    JSON Responses: All responses are formatted in JSON to ensure easy parsing by clients.

    Root Endpoint: The root endpoint provides a welcome message or a filtered movie list based on the genre passed as a query parameter.

## Installation
To install this project, make sure Python 3.x and Flask are installed. Place movies.csv in the project directory, then install Flask using pip install Flask.

## Usage
Start the application by running python app.py and access it at http://localhost:8080/. To view movies by genre, use http://localhost:8080/?genre=GENRE_NAME or navigate directly to genre endpoints like http://localhost:8080/action.


### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>

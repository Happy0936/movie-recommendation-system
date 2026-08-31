# Movie Recommendation System

A Content-Based Movie Recommendation System built using Python, Pandas, Scikit-Learn, and Streamlit. The system recommends movies similar to a selected movie by analyzing genres, cast, crew, keywords, and movie overviews using Cosine Similarity.

---

## Features

* Recommend Top 5 similar movies
* Content-Based Filtering
* Cosine Similarity based recommendations
* Interactive Streamlit Web Application
* User-friendly movie selection interface
* Fast recommendation generation

---

## Tech Stack

### Programming Language

* Python

### Libraries Used

* Pandas
* NumPy
* Scikit-Learn
* NLTK
* Streamlit
* Pickle

### Dataset

* TMDB 5000 Movies Dataset
* TMDB 5000 Credits Dataset

---

## Project Workflow

### Data Collection

The project uses the TMDB Movie Metadata Dataset containing movie information such as:

* Movie Title
* Genres
* Cast
* Crew
* Keywords
* Overview

### Data Collection & Backend Processing

The backend logic processes data from the TMDB Movie Metadata Dataset, covering the following stages:

**Data Preprocessing**: Merged movies and credits datasets, removed missing values, extracted key features (Genres, Keywords, Top Cast Members, Director), combined all features into a single tags column, converted text into lowercase, and applied stemming using NLTK.

**Feature Engineering & Vectorization**: Combined text features (Overview, Genres, Keywords, Cast, Director) into a unified tags column and utilized CountVectorizer to transform textual data into numerical vectors.

**Similarity Calculation**: Applied Cosine Similarity to compute similarity scores between movies to generate accurate recommendations.

**Model Serialization**: Serialized trained data models and mappings into binary files (movie_list.pkl, similarity.pkl) using Python's pickle library.

### Feature Engineering

A tags column was created by combining:

* Overview
* Genres
* Keywords
* Cast
* Director

### Vectorization

CountVectorizer was used to convert text data into numerical vectors.

### Similarity Calculation

Cosine Similarity was used to measure similarity between movies and generate recommendations.

---

## Recommendation Process

1. User selects a movie.
2. System finds the movie index.
3. Cosine similarity scores are calculated.
4. Top 5 most similar movies are identified.
5. Recommendations are displayed to the user.

---

## Project Structure

movie-recommendation-system/

├── app.py

├── movie_list.pkl

├── similarity.pkl

├── requirements.txt

├── README.md

├── MoviesData/

│   ├── tmdb_5000_movies.csv

│   └── tmdb_5000_credits.csv

└── Home/

```
└── background.jpg
```

---

## Run Locally

### Clone Repository

git clone <repository-url>

### Move into Project Directory

cd movie-recommendation-system

### Install Dependencies

pip install -r requirements.txt

### Run Streamlit App

streamlit run app.py

---

## Sample Recommendation

Input Movie:

Avengers: Age of Ultron

Recommended Movies:

* Iron Man
* Iron Man 3
* The Avengers
* Captain America: Civil War
* Iron Man 2

---

## Learning Outcomes

Through this project, I learned:

* Data Preprocessing
* Feature Engineering
* Natural Language Processing Basics
* CountVectorizer
* Cosine Similarity
* Model Serialization using Pickle
* Streamlit Web App Development
* Git & GitHub
* Project Deployment

---

## Future Improvements

* Movie Posters Integration using TMDB API
* Movie Ratings Display
* Genre-based Filtering
* Search Suggestions
* Netflix-style User Interface
* Cloud Deployment

---

## Author

Happy

M.Tech Student

Machine Learning & Data Science Enthusiast

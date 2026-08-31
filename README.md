# Movie Recommendation System

A **Content-Based Movie Recommendation System** built using **Python, Pandas, Scikit-Learn, and Streamlit**.

The system recommends movies similar to a selected movie by analyzing **genres, cast, crew, keywords, and movie overviews** using **CountVectorizer and Cosine Similarity**.

---

##  Live Demo

🔹 **Streamlit Web App**  
👉 https://movie-recommender-happy.streamlit.app/


---

## Features

-  **Top 5 Recommendations**  
  Get the top 5 movies similar to the selected movie.

-  **Content-Based Filtering**  
  Recommendations are generated based on movie content and features.

-  **Cosine Similarity**  
  Calculates similarity between movies using their feature vectors.

-  **Interactive Movie Search**  
  Select a movie easily using the Streamlit interface.

-  **Movie Poster Integration**  
  Fetches movie posters dynamically using the TMDB API.

-  **OTT Availability Search**  
  Provides a direct search option to find where the selected movie is available for streaming.

-  **Secure API Configuration**  
  TMDB API credentials are stored securely using Streamlit Secrets.

-  **Fast Recommendations**  
  Pre-computed similarity data allows recommendations to be generated quickly.

---

##  Tech Stack

### Programming Language

- Python

### Libraries & Frameworks

- **Pandas** – Data manipulation and preprocessing
- **NumPy** – Numerical computation
- **Scikit-Learn** – CountVectorizer and Cosine Similarity
- **NLTK** – Text preprocessing and stemming
- **Streamlit** – Interactive web application
- **Requests** – TMDB API requests
- **Pickle** – Model and data serialization

### APIs

- **TMDB API** – Movie posters and movie metadata

### Tools

- Git
- GitHub
- Streamlit Community Cloud
- Jupyter Notebook

---

##  Dataset

This project uses the **TMDB 5000 Movie Dataset**, consisting of:

- **TMDB 5000 Movies Dataset**
- **TMDB 5000 Credits Dataset**

### Movie Information Used

The dataset contains information such as:

- Movie Title
- Movie Overview
- Genres
- Keywords
- Cast
- Crew
- Director
- Movie ID

---

#  Project Workflow

## 1. Data Collection

The project uses the TMDB 5000 Movies and Credits datasets containing detailed movie information.

The important features used for recommendation include:

- Movie Title
- Overview
- Genres
- Keywords
- Cast
- Director

---

## 2. Data Preprocessing

The movies and credits datasets are merged using the movie ID.

The following preprocessing steps are performed:

- Merge movies and credits datasets
- Remove unnecessary columns
- Handle missing values
- Extract genres
- Extract keywords
- Extract top cast members
- Extract director
- Convert text into lowercase
- Apply stemming using NLTK

---

## 3. Feature Engineering

Different movie features are combined into a single **`tags`** column.

The tags contain:

- Overview
- Genres
- Keywords
- Cast
- Director

This allows the recommendation system to compare movies based on their overall content.

---

## 4. Text Vectorization

The combined `tags` column is converted into numerical vectors using **CountVectorizer** from Scikit-Learn.

This transforms the textual movie information into a mathematical representation that can be compared.

---

## 5. Similarity Calculation

**Cosine Similarity** is used to calculate the similarity between movie vectors.

Movies with higher similarity scores are considered more closely related.

The resulting similarity matrix is stored in:

```text
similarity.pkl
```
---
## **Project Structure**
```text
movie-recommendation-system/
│
├── MoviesData/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── app.py
├── main.py
├── movie recommendation.ipynb
├── movie_list.pkl
├── similarity.pkl
├── requirements.txt
├── .gitignore
├── .gitattributes
└── README.md
```


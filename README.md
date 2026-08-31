# Movie Recommendation System

A **Content-Based Movie Recommendation System** built using **Python, Scikit-Learn, Pandas, NLTK, and Streamlit**.  
It recommends the **Top 5 similar movies** based on movie content using **CountVectorizer and Cosine Similarity**.

---

## Live Demo

👉 **Streamlit App:** YOUR_STREAMLIT_URL

---

## Features

-  **Top 5 Movie Recommendations**
-  **Content-Based Recommendation**
-  **Cosine Similarity**
-  **Interactive Movie Search using Streamlit**
-  **Dynamic Movie Posters using TMDB API**
-  **OTT Availability Search**
-  **Secure TMDB API Key using Streamlit Secrets**

---

## Tech Stack

- **Python**
- **Pandas & NumPy**
- **Scikit-Learn** – CountVectorizer, Cosine Similarity
- **NLTK** – Text preprocessing & stemming
- **Streamlit** – Web Application
- **Requests** – TMDB API integration
- **Pickle** – Model serialization
- **TMDB API** – Movie posters

---

## Dataset

The project uses the **TMDB 5000 Movie Dataset**:

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

### Features Used

- Movie Overview
- Genres
- Keywords
- Cast
- Director

---

## Project Workflow

### Data Preprocessing

- Merged the Movies and Credits datasets.
- Extracted genres, keywords, top cast members, and director.
- Handled missing values.
- Converted text to lowercase.
- Applied stemming using NLTK.

### Feature Engineering

Combined **Overview, Genres, Keywords, Cast, and Director** into a single `tags` column.

### Vectorization

Used **CountVectorizer** to convert movie tags into numerical vectors.

### Similarity Calculation

Used **Cosine Similarity** to calculate similarity between movies and generate recommendations.

The pre-computed similarity matrix is stored in:

```text
similarity.pkl
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
---
## **Run Locally**  
   Clone the repository:
   ```bash
   git clone https://github.com/Happy0936/movie_recommendation_system.git
   cd movie_recommendation_system
   ```
   Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```


### **Configure TMDB API**
   Create:
   ```bash
   .streamlit/secrets.toml
   ```
   Add your API key:
   ```bash
   TMDB_API_KEY = "your_api_key_here"
   ```
   Run Application:
   ```bash
   python -m streamlit run app.py
```bash

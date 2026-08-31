import streamlit as st
import pickle
import requests
import urllib.parse
import pandas as pd

# ----------------- PAGE CONFIGURATION -----------------
# Yahan naam wapas Movie Recommendation kar diya gaya hai
st.set_page_config(page_title="Movie Recommendation", page_icon="🎬", layout="wide")

# ----------------- CUSTOM CSS STYLING (Premium Theme) -----------------
st.markdown("""
    <style>
    /* HIDE STREAMLIT DEPLOY BUTTON AND MENU */
 /*   #MainMenu {visibility: hidden;}*/
    /*   footer {visibility: hidden;}*/
   /*    header {visibility: hidden;}*/

    /* INCREASED TOP PADDING TO PREVENT CUTTING OFF */
    .block-container {
        padding-top: 3.5rem !important;
        padding-bottom: 2rem !important;
    }
    
    /* Super Dark Theme matching the image */
    .stApp {
        background-color: #0b0e14;
        color: #e2e8f0;
    }
    .stSelectbox label, .stMarkdown, p, h1, h2, h3 {
        color: #e2e8f0 !important;
    }
    
    /* Top Navigation Bar Styling */
    .top-nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-bottom: 12px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        margin-bottom: 40px;
    }
    .brand-logo {
        font-size: 22px;
        font-weight: 800;
        color: #ffffff;
        display: flex;
        align-items: center;
        gap: 8px;
        letter-spacing: -0.5px;
    }
    .status-badge {
        background-color: rgba(255,255,255,0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 13px;
        color: #94a3b8;
        font-weight: 500;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .status-dot {
        height: 8px;
        width: 8px;
        background-color: #f87171; 
        border-radius: 50%;
        display: inline-block;
    }
    
    /* Hero Typography - Centered */
    .hero-container {
        text-align: center;
        margin-bottom: 40px;
    }
    .hero-title {
        font-size: 48px;
        font-weight: 800;
        color: #f1f5f9;
        line-height: 1.2;
        margin-bottom: 15px;
        letter-spacing: -1px;
    }
    .hero-subtitle {
        font-size: 16px;
        color: #94a3b8;
        max-width: 650px;
        margin: 0 auto;
        line-height: 1.6;
    }
    
    /* Primary Explore Button (Purple) */
    div.stButton > button[kind="primary"] {
        background-color: #6366f1; 
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        height: 42px;
        width: 100%;
        transition: 0.3s;
    }
    div.stButton > button[kind="primary"]:hover {
        background-color: #4f46e5;
        color: white;
    }
    
    /* Secondary Trending Buttons */
    div.stButton > button[kind="secondary"] {
        background-color: transparent;
        color: #94a3b8;
        border: 1px solid #334155;
        border-radius: 20px;
        height: 36px;
        padding: 0px 15px;
        transition: 0.3s;
    }
    div.stButton > button[kind="secondary"]:hover {
        border-color: #6366f1;
        color: white;
    }
    
    /* Watch/Trailer Link Button & OTT */
    div.stLinkButton > a {
        background-color: #1e293b;
        color: white;
        border-radius: 4px;
        text-align: center;
        text-decoration: none;
        padding: 0.4rem;
        font-size: 13px;
        font-weight: bold;
        width: 100%;
        display: block;
        border: 1px solid #334155;
    }
    div.stLinkButton > a:hover {
        background-color: #6366f1;
        border-color: #6366f1;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- LOAD DATASET -----------------
try:
    movies = pickle.load(open('movie_list.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    movie_titles = list(movies['title'].values)
except FileNotFoundError:
    st.error("⚠️ Dataset not found. Ensure 'movie_list.pkl' and 'similarity.pkl' are in the same directory.")
    st.stop()

# ----------------- FUNCTIONS -----------------
def fetch_poster(movie_id):
    poster_url = "https://via.placeholder.com/500x750?text=No+Poster"
    API_KEY = "3ba3dc8532c0d5c44713853736ef5a24"
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
        data = requests.get(url).json()
        poster_path = data.get('poster_path')
        if poster_path:
            poster_url = f"https://image.tmdb.org/t/p/w500/{poster_path}"
    except Exception:
        pass
    return poster_url

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_posters = []
    recommended_links = []
    
    for i in movies_list:
        row = movies.iloc[i[0]]
        movie_id = row.movie_id
        title = row.title
        
        poster = fetch_poster(movie_id)
        
        recommended_movies.append(title)
        recommended_posters.append(poster)
        
        query = urllib.parse.quote(f"{title} full movie watch online or trailer")
        recommended_links.append(f"https://www.youtube.com/results?search_query={query}")
        
    return recommended_movies, recommended_posters, recommended_links

# ----------------- STATE INITIALIZATION -----------------
if "selected_movie" not in st.session_state:
    st.session_state["selected_movie"] = movie_titles[0]
if "trigger_recommendation" not in st.session_state:
    st.session_state["trigger_recommendation"] = False

# =====================================================================
# 1. EXACT IMAGE NAV BAR (Logo + Pill Badge)
# =====================================================================
# Yahan nav bar me bhi wapas Movie Recommendation update kiya hai
st.markdown("""
<div class="top-nav">
    <div class="brand-logo"><span style="color:#6366f1;">🎬</span> Movie Recommendation</div>
    <div class="status-badge"><span class="status-dot"></span> API Disconnected</div>
</div>
""", unsafe_allow_html=True)

# =====================================================================
# 2. HERO SECTION (Centered Layout like image)
# =====================================================================
st.markdown("""
<div class="hero-container">
    <div class="hero-title">Discover Your Next Favorite<br>Movie</div>
    <div class="hero-subtitle">Type any movie title below to receive tailored content-based recommendations along<br>with direct streaming links across major OTT platforms.</div>
</div>
""", unsafe_allow_html=True)

# ----------------- SEARCH ROW -----------------
search_col, btn_col = st.columns([4, 1.2])

with search_col:
    try:
        current_index = movie_titles.index(st.session_state["selected_movie"])
    except ValueError:
        current_index = 0

    selected_movie = st.selectbox(
        label="search_box",
        options=movie_titles,
        index=current_index,
        label_visibility="collapsed"
    )
    st.session_state["selected_movie"] = selected_movie

with btn_col:
    if st.button("Explore ➔", type="primary"):
        st.session_state["trigger_recommendation"] = True

# ----------------- TRENDING PICKS -----------------
st.write("") 
spacer1, pop_text, chip1, chip2, chip3, chip4, spacer2 = st.columns([1, 0.8, 1, 1.5, 1.2, 1, 1])

with pop_text:
    st.markdown("<p style='color: #64748b; font-size: 14px; text-align: right; margin-top: 8px;'>Popular:</p>", unsafe_allow_html=True)

trending_list = ["Avatar", "The Dark Knight", "Interstellar", "Inception"]
chip_columns = [chip1, chip2, chip3, chip4]

for idx, title in enumerate(trending_list):
    with chip_columns[idx]:
        if title in movie_titles:
            if st.button(title, key=f"chip_{idx}"):
                st.session_state["selected_movie"] = title
                st.session_state["trigger_recommendation"] = True
                st.rerun()

st.markdown("<div style='margin-bottom: 50px;'></div>", unsafe_allow_html=True)

# =====================================================================
# 3. RECOMMENDATIONS & OTT SEARCH 
# =====================================================================
if st.session_state["trigger_recommendation"]:
    with st.spinner("Finding best recommendations for you..."):
        names, posters, links = recommend(st.session_state["selected_movie"])
        
        st.markdown("### Top Recommendations for You")
        cols = st.columns(5)
        
        for idx, col in enumerate(cols):
            with col:
                st.image(posters[idx], use_container_width=True)
                st.markdown(f"**{names[idx]}**")
                st.link_button("▶ Watch / Trailer", links[idx])
    
    st.markdown("---")
    
    # OTT Availability Finder
    st.markdown("### 🌐 OTT Availability Finder")
    st.write(f"Search Google to find where **{st.session_state['selected_movie']}** is streaming (Netflix, Prime Video, Disney+ Hotstar, etc.):")
    
    google_query = urllib.parse.quote(f"watch {st.session_state['selected_movie']} online streaming ott netflix prime hotstar")
    google_url = f"https://www.google.com/search?q={google_query}"
    
    st.markdown(
        f"<a href='{google_url}' target='_blank' style='display: inline-block; padding: 10px 20px; background-color: #1e293b; color: white; border: 1px solid #334155; border-radius: 8px; text-decoration: none; font-weight: bold;'>🔍 Search Streaming Platforms on Google</a>",
        unsafe_allow_html=True
    )
import pickle

import numpy as np
import streamlit as st

# Add custom CSS for improved UI styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Poppins:wght@300;400;500;600&display=swap');
    
    /* Global styles and fonts */
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Overall background with hero image */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)),
                    url('https://images.unsplash.com/photo-1507842217343-583bb7270b66?w=1600');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #ffffff;
    }
    
    /* Header styling */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Playfair Display', serif;
        color: #ffffff;
        font-weight: 700;
        letter-spacing: -0.5px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    /* Hero section */
    .hero-section {
        text-align: center;
        padding: 40px 20px;
        margin-bottom: 30px;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Styling for buttons */
    div.stButton > button {
        background: linear-gradient(135deg, #2C3E50 0%, #3498DB 100%);
        color: white;
        border-radius: 30px;
        padding: 15px 35px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        font-size: 18px;
        font-weight: 600;
        transition: all 0.4s ease;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    
    div.stButton > button:hover {
        background: linear-gradient(135deg, #3498DB 0%, #2C3E50 100%);
        box-shadow: 0 8px 25px rgba(52, 152, 219, 0.4);
        transform: translateY(-3px);
        border-color: rgba(255, 255, 255, 0.2);
    }
    
    /* Styling for selectbox contents */
    div[data-baseweb="select"] {
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        background: rgba(0, 0, 0, 0.6);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        color: white !important;
    }
    
    /* Ensure text is white in select input */
    div[data-baseweb="select"] span {
        color: white !important;
    }
    
    /* Style the placeholder text */
    div[data-baseweb="select"] [data-testid="stSelectbox"] {
        color: white !important;
    }
    
    div[data-baseweb="select"]:hover {
        border-color: rgba(255, 255, 255, 0.4);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }
    
    /* Custom styling for select dropdown text */
    .stSelectbox div[role="listbox"] div[role="option"] {
        color: white !important;
        background: rgba(0, 0, 0, 0.8);
    }
    
    /* Style for the select input container */
    .stSelectbox > div > div {
        background: rgba(0, 0, 0, 0.6) !important;
    }
    
    /* Style for select box label */
    .stSelectbox label {
        color: white !important;
        font-size: 1.1em !important;
        font-weight: 500 !important;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
    }
    
    /* Ensure dropdown options are clearly visible */
    .stSelectbox div[role="listbox"] {
        background: rgba(0, 0, 0, 0.9) !important;
    }
    
    /* Book recommendation card styling */
    .book-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(12px);
        border-radius: 25px;
        padding: 15px;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        margin: 10px;
        height: 350px;
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .book-card:hover {
        transform: translateY(-15px) scale(1.03);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4);
        border-color: rgba(255, 255, 255, 0.4);
        background: rgba(255, 255, 255, 0.2);
    }
    
    .book-title {
        font-size: 18px;
        font-weight: 600;
        color: #ffffff;
        margin-top: 15px;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        line-height: 1.5;
        padding: 15px 10px;
    }
    
    /* Loading spinner customization */
    .stSpinner {
        text-align: center;
        max-width: 50%;
        margin: 0 auto;
    }
    </style>
    """, unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div class="hero-section">
        <h1>📚 Book Recommender System</h1>
        <p style="font-size: 1.2em; opacity: 0.9;">Discover your next favorite book using the power of Machine Learning</p>
    </div>
""", unsafe_allow_html=True)

# Load models and data
model = pickle.load(open(r'pkl files\model.pkl','rb'))
book_names = pickle.load(open(r'pkl files\books_name.pkl','rb'))
final_rating = pickle.load(open(r'pkl files\final_rating.pkl','rb'))
book_pivot = pickle.load(open(r'pkl files\book_pivote.pkl','rb'))

def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])

    for name in book_name[0]: 
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['img_url']
        poster_url.append(url)

    return poster_url

def recommend_book(book_name):
    books_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6 )

    poster_url = fetch_poster(suggestion)
    
    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            books_list.append(j)
    return books_list, poster_url       

# Main container layout
with st.container():
    st.subheader("📖 Find Similar Books")
    # A selectbox for book selection
    selected_book = st.selectbox(
        "Enter a book you enjoyed reading",
        book_names,
        help="Start typing a book title or use the dropdown to select a book you've read and enjoyed"
    )
    st.caption("Based on your selection, we'll recommend similar books you might love! 💫")

    if st.button('Show Recommendation'):
        with st.spinner('Finding the best book recommendations for you...'):
            recommended_books, poster_url = recommend_book(selected_book)
            
            # Create a container for the recommendations grid
            recommendation_container = st.container()
            with recommendation_container:
                # Use columns for a nice layout
                cols = st.columns(5)  # Display 5 books in a row
                for idx, col in enumerate(cols[:5]):  # Ensure we only show 5 books
                    with col:
                        # Create a card for each book
                        st.markdown(f"""
                            <div class="book-card">
                                <img src="{poster_url[idx]}" style="width: 100%; height: 250px; object-fit: cover; border-radius: 8px;">
                                <div class="book-title">{recommended_books[idx]}</div>
                            </div>
                            """, unsafe_allow_html=True)

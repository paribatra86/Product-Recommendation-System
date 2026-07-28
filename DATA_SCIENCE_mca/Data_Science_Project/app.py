import streamlit as st
import pandas as pd

from utils import load_data, apriori_recommend
from dashboard import show_dashboard
from recommendation import recommendation_page

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Product Recommendation System",
    page_icon="🛍️",
    layout="wide"
)

# -------------------------------
# LOAD DATA
# -------------------------------
df = load_data()

from pathlib import Path

BASE_DIR = Path(__file__).parent

@st.cache_data
def load_rules():
    return pd.read_pickle(BASE_DIR / "rules.pkl")

rules = load_rules()

rules = load_rules()
# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "Dashboard",
        "Recommendation"
    ]
)

# -------------------------------
# HOME PAGE
# -------------------------------
if page == "Home":

    st.title("🛍️ Product Recommendation System")

    st.markdown("---")

    st.header("Project Overview")

    st.write("""
This project recommends products based on customers' purchasing behavior.

### Algorithms Used

- Popularity-Based Recommendation
- Item-Based Collaborative Filtering
- Association Rule Mining (Apriori Algorithm)

The dashboard summarizes business performance while the recommendation
engine suggests products frequently purchased together.
""")

    st.markdown("---")

    st.subheader("Dataset Information")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", len(df))
    col2.metric("Products", df["StockCode"].nunique())
    col3.metric("Customers", df["CustomerID"].nunique())

    st.markdown("---")

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

# -------------------------------
# DASHBOARD
# -------------------------------
elif page == "Dashboard":

    show_dashboard(df)

# -------------------------------
# RECOMMENDATION
# -------------------------------
elif page == "Recommendation":

    recommendation_page(
        df,
        rules,
        apriori_recommend
    )

# -------------------------------
# FOOTER
# -------------------------------
st.sidebar.markdown("---")
st.sidebar.success("Developed using Streamlit")
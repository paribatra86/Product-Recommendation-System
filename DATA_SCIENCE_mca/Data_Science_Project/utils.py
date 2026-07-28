import streamlit as st
import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).parent

@st.cache_data
def load_data():
    df = pd.read_csv(BASE_DIR / "Online_Retail.csv")
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], format="mixed")
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]
    return df

def apriori_recommend(rules, product_name, n=5):

    recommendation = rules[
        rules["antecedents"].apply(lambda x: product_name in x)
    ]

    if recommendation.empty:
        return None

    recommendation = recommendation.sort_values(
        by="lift",
        ascending=False
    ).head(n)

    recommendation = recommendation.copy()

    recommendation["Recommended Product"] = recommendation[
        "consequents"
    ].apply(lambda x: ", ".join(list(x)))

    return recommendation[
        [
            "Recommended Product",
            "support",
            "confidence",
            "lift",
        ]
    ]
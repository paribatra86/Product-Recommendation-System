import streamlit as st


def recommendation_page(df, rules, recommend_function):

    st.header("🛍 Product Recommendation")

    products = sorted(df["Description"].dropna().unique())

    selected = st.selectbox(
        "Select Product",
        products
    )

    if st.button("Get Recommendation"):

        result = recommend_function(
            rules,
            selected
        )

        if result is None:

            st.warning("No Recommendation Found")

        else:

            st.dataframe(result)
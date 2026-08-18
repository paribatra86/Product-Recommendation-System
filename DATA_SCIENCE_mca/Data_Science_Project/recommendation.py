import streamlit as st


def recommendation_page(rules, recommend_function):

    st.header("🛍 Product Recommendation")

    products = sorted(
        {
            item
            for antecedent in rules["antecedents"]
            for item in antecedent
        }
    )

    selected = st.selectbox(
        "Select Product",
        products
    )

    if st.button("Get Recommendation"):

        result = recommend_function(
            rules,
            selected
        )

        if result is None or len(result) == 0:
            st.warning("No Recommendation Found")

        else:
            st.success("Recommended Products")
            st.dataframe(result)

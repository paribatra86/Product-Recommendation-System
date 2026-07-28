import streamlit as st
import matplotlib.pyplot as plt


def show_dashboard(df):

    st.header("📊 Dashboard")

    revenue = df["TotalPrice"].sum()
    orders = df["InvoiceNo"].nunique()
    customers = df["CustomerID"].nunique()
    products = df["StockCode"].nunique()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Revenue", f"£{revenue:,.0f}")
    c2.metric("Orders", orders)
    c3.metric("Customers", customers)
    c4.metric("Products", products)

    monthly = (
        df.groupby(df["InvoiceDate"].dt.to_period("M"))["TotalPrice"]
        .sum()
    )

    top_products = (
        df.groupby("Description")["Quantity"]
        .sum()
        .sort_values(ascending=False)
        .head(8)
    )

    country = (
        df.groupby("Country")["TotalPrice"]
        .sum()
        .sort_values(ascending=False)
        .head(8)
    )

    fig, ax = plt.subplots(2,2,figsize=(14,10))

    ax[0,0].plot(monthly.index.astype(str),monthly.values,marker="o")
    ax[0,0].set_title("Monthly Sales")

    ax[0,1].barh(top_products.index,top_products.values)
    ax[0,1].set_title("Top Products")

    ax[1,0].bar(country.index,country.values)
    ax[1,0].tick_params(axis="x",rotation=45)
    ax[1,0].set_title("Country Revenue")

    ax[1,1].axis("off")
    ax[1,1].text(
        0,
        1,
        """
Business Insights

• UK generates maximum revenue.

• Few products dominate sales.

• Monthly trend shows seasonality.

• Apriori recommends products
frequently purchased together.
        """,
        fontsize=12
    )

    st.pyplot(fig)
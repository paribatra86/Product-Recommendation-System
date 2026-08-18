import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


def show_dashboard(df):

    st.header("📊 Dashboard")

    # ---------------- Data Validation ---------------- #

    df = df.copy()

    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    df = df.dropna(subset=["Description"])


    # ---------------- KPI Cards ---------------- #

    revenue = df["TotalPrice"].sum()
    orders = df["InvoiceNo"].nunique()
    customers = df["CustomerID"].nunique()
    products = df["StockCode"].nunique()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("💰 Revenue", f"£{revenue:,.0f}")
    c2.metric("🧾 Orders", f"{orders:,}")
    c3.metric("👥 Customers", f"{customers:,}")
    c4.metric("📦 Products", f"{products:,}")


    st.divider()


    # ---------------- Data Preparation ---------------- #

    monthly = (
        df.groupby(
            df["InvoiceDate"].dt.to_period("M")
        )["TotalPrice"]
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


    # ---------------- Monthly Sales Chart ---------------- #

    st.subheader("📈 Monthly Sales Trend")

    fig1, ax1 = plt.subplots(figsize=(10,4))

    ax1.plot(
        monthly.index.astype(str),
        monthly.values,
        marker="o"
    )

    ax1.set_xlabel("Month")
    ax1.set_ylabel("Revenue")
    ax1.tick_params(axis="x", rotation=45)

    plt.tight_layout()

    st.pyplot(fig1)



    # ---------------- Product Analysis ---------------- #

    st.subheader("🏆 Top Selling Products")

    fig2, ax2 = plt.subplots(figsize=(10,5))

    ax2.barh(
        top_products.index[::-1],
        top_products.values[::-1]
    )

    ax2.set_xlabel("Quantity Sold")

    plt.tight_layout()

    st.pyplot(fig2)



    # ---------------- Country Revenue ---------------- #

    st.subheader("🌍 Revenue by Country")

    fig3, ax3 = plt.subplots(figsize=(10,5))

    ax3.bar(
        country.index,
        country.values
    )

    ax3.set_ylabel("Revenue")
    ax3.tick_params(axis="x", rotation=45)

    plt.tight_layout()

    st.pyplot(fig3)



    # ---------------- Business Insights ---------------- #

    st.subheader("💡 Business Insights")

    st.info(
        """
        • United Kingdom contributes the highest revenue.

        • A few products generate a major portion of sales.

        • Sales trends help identify seasonal patterns.

        • Apriori discovers frequently purchased product combinations.

        • Recommendations can improve cross-selling opportunities.
        """
    )

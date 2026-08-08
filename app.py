import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Delivery Performance Dashboard",
    page_icon="🚚",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv("compressed_data.csv.gz", compression="gzip")

    # Generate synthetic Order Date (dataset has no real date fields)
    np.random.seed(42)
    start_date = pd.Timestamp("2015-01-01")
    end_date = pd.Timestamp("2018-01-31")
    date_range_days = (end_date - start_date).days

    random_offsets = np.random.randint(0, date_range_days, size=len(df))
    df["Order Date"] = start_date + pd.to_timedelta(random_offsets, unit="D")
    df["Shipping Date"] = df["Order Date"] + pd.to_timedelta(df["Days for shipping (real)"], unit="D")

    return df

df = load_data()

df = load_data()

st.sidebar.header("🔍 Filters")

selected_mode = st.sidebar.multiselect(
    "Shipping Mode",
    options=df["Shipping Mode"].unique(),
    default=df["Shipping Mode"].unique()
)

selected_market = st.sidebar.multiselect(
    "Market",
    options=df["Market"].unique(),
    default=df["Market"].unique()
)

selected_region = st.sidebar.multiselect(
    "Order Region",
    options=df["Order Region"].unique(),
    default=df["Order Region"].unique()
)

selected_segment = st.sidebar.multiselect(
    "Customer Segment",
    options=df["Customer Segment"].unique(),
    default=df["Customer Segment"].unique()
)

df["Order Date"] = pd.to_datetime(df["Order Date"])

min_date = df["Order Date"].min()
max_date = df["Order Date"].max()

selected_date_range = st.sidebar.date_input(
    "Order Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

st.sidebar.caption("⚠️ Order dates are simulated — the provided dataset did not include real date fields.")

# Apply filters to create a working dataframe
filtered_df = df[
    (df["Shipping Mode"].isin(selected_mode)) &
    (df["Market"].isin(selected_market)) &
    (df["Order Region"].isin(selected_region)) &
    (df["Customer Segment"].isin(selected_segment)) &
    (df["Order Date"] >= pd.to_datetime(selected_date_range[0])) &
    (df["Order Date"] <= pd.to_datetime(selected_date_range[1]))
]

st.title("🚚 Delivery Performance, Delay Risk & Logistics Efficiency Dashboard")
st.markdown("**APL Logistics** | Global Supply Chain Operations Analysis")
st.markdown("---")

on_time_rate = (filtered_df["Delivery_Class"] == "On-time").mean() * 100
late_risk_ratio = filtered_df["Late_delivery_risk"].mean() * 100
avg_delay = filtered_df["Delay_Gap"].mean()
total_orders = len(filtered_df)

if filtered_df.empty:
    st.warning("⚠️ No data matches the selected filters. Please adjust your selection.")
    st.stop()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Orders", f"{total_orders:,}")
col2.metric("On-Time Delivery Rate", f"{on_time_rate:.2f}%")
col3.metric("Late Delivery Risk", f"{late_risk_ratio:.2f}%")
col4.metric("Avg Delivery Delay", f"{avg_delay:.2f} days")

st.markdown("---")

# CHARTS SECTION

st.subheader("📊 Delivery Performance Overview")

col1, col2 = st.columns(2)

with col1:
    class_counts = filtered_df["Delivery_Class"].value_counts().reset_index()
    class_counts.columns = ["Delivery_Class", "Count"]
    fig1 = px.pie(class_counts, names="Delivery_Class", values="Count",
                  title="On-time vs Delayed vs Early",
                  color="Delivery_Class",
                  color_discrete_map={"Delayed": "#e74c3c", "Early": "#3498db", "On-time": "#2ecc71"})
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.histogram(filtered_df, x="Delay_Gap", nbins=15,
                         title="Delay Gap Distribution")
    fig2.add_vline(x=0, line_dash="dash", line_color="red")
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")
st.subheader("🚛 Shipping Mode Comparison")

mode_risk = filtered_df.groupby("Shipping Mode")["Late_delivery_risk"].mean().reset_index()
mode_risk["Late_delivery_risk"] = mode_risk["Late_delivery_risk"] * 100
mode_risk = mode_risk.sort_values("Late_delivery_risk", ascending=False)

fig3 = px.bar(mode_risk, x="Shipping Mode", y="Late_delivery_risk",
              title="Late Delivery Risk (%) by Shipping Mode",
              color="Late_delivery_risk", color_continuous_scale="Reds")
st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")
st.subheader("🌍 Regional Risk Analysis")

region_risk = filtered_df.groupby("Order Region")["Late_delivery_risk"].mean().reset_index()
region_risk["Late_delivery_risk"] = region_risk["Late_delivery_risk"] * 100
region_risk = region_risk.sort_values("Late_delivery_risk", ascending=False)

fig4 = px.bar(region_risk, x="Late_delivery_risk", y="Order Region", orientation="h",
              title="Late Delivery Risk (%) by Order Region",
              color="Late_delivery_risk", color_continuous_scale="Reds")
st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")
st.subheader(" Region × Shipping Mode Risk Heatmap")

heatmap_data = filtered_df.groupby(["Order Region", "Shipping Mode"])["Late_delivery_risk"].mean().unstack() * 100

fig5 = px.imshow(heatmap_data,
                  text_auto=".0f",
                  color_continuous_scale="Reds",
                  aspect="auto",
                  labels=dict(x="Shipping Mode", y="Order Region", color="Late Risk (%)"))
fig5.update_layout(title="Late Delivery Risk (%): Region × Shipping Mode")
st.plotly_chart(fig5, use_container_width=True)
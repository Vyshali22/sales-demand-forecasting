import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import os

st.set_page_config(page_title="Sales Demand Forecasting", page_icon="📊", layout="wide")

st.markdown("""
<style>
    .main-header {font-size: 2.2rem; font-weight: bold; color: #1565C0; text-align: center; margin-bottom: 0.2rem;}
    .sub-header {font-size: 1rem; color: #555; text-align: center; margin-bottom: 2rem;}
    .metric-card {background: #f0f4ff; border-radius: 10px; padding: 1rem; text-align: center;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">📊 Sales Demand Forecasting Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Interactive Analytics & Revenue Prediction | Python + Machine Learning</div>', unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, '..', 'data', 'sales_data.csv')
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year
    df['DayOfWeek'] = df['Date'].dt.dayofweek
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("🔍 Filters")
categories = st.sidebar.multiselect("Category", df['Category'].unique(), default=list(df['Category'].unique()))
regions = st.sidebar.multiselect("Region", df['Region'].unique(), default=list(df['Region'].unique()))
years = st.sidebar.multiselect("Year", sorted(df['Year'].unique()), default=list(df['Year'].unique()))

filtered = df[df['Category'].isin(categories) & df['Region'].isin(regions) & df['Year'].isin(years)]

# KPI Metrics
st.subheader("📈 Key Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"₹{filtered['Revenue'].sum():,.0f}")
col2.metric("Total Orders", f"{len(filtered):,}")
col3.metric("Avg Order Value", f"₹{filtered['Revenue'].mean():,.0f}")
col4.metric("Avg Discount", f"{filtered['Discount'].mean()*100:.1f}%")

st.divider()

# Charts Row 1
st.subheader("📊 Sales Analysis")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Revenue by Category**")
    cat_rev = filtered.groupby('Category')['Revenue'].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(cat_rev.index, cat_rev.values, color=['#2196F3','#4CAF50','#FF9800','#E91E63','#9C27B0'])
    ax.set_ylabel("Revenue (₹)")
    ax.tick_params(axis='x', rotation=15)
    st.pyplot(fig)
    plt.close()

with col2:
    st.markdown("**Revenue by Region**")
    reg_rev = filtered.groupby('Region')['Revenue'].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(reg_rev.index, reg_rev.values, color=['#F44336','#00BCD4','#8BC34A','#FF5722'])
    ax.set_ylabel("Revenue (₹)")
    st.pyplot(fig)
    plt.close()

# Charts Row 2
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Monthly Revenue Trend**")
    monthly = filtered.groupby(['Year','Month'])['Revenue'].sum().reset_index()
    monthly['Period'] = monthly['Year'].astype(str) + '-' + monthly['Month'].astype(str).str.zfill(2)
    monthly = monthly.sort_values('Period')
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(monthly['Period'], monthly['Revenue'], marker='o', color='#2196F3', linewidth=2)
    ax.tick_params(axis='x', rotation=45)
    ax.set_ylabel("Revenue (₹)")
    st.pyplot(fig)
    plt.close()

with col2:
    st.markdown("**Top 10 Products by Revenue**")
    top_prod = filtered.groupby('Product')['Revenue'].sum().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.barh(top_prod.index, top_prod.values, color='#4CAF50')
    ax.set_xlabel("Revenue (₹)")
    st.pyplot(fig)
    plt.close()

st.divider()

# Correlation Heatmap
st.subheader("🔗 Correlation Heatmap")
numeric_cols = ['Units_Sold', 'Unit_Price', 'Revenue', 'Discount', 'Customer_Age', 'Month']
fig, ax = plt.subplots(figsize=(8, 4))
sns.heatmap(filtered[numeric_cols].corr(), annot=True, fmt='.2f', cmap='coolwarm', ax=ax)
st.pyplot(fig)
plt.close()

st.divider()

# Revenue Predictor
st.subheader("🤖 Revenue Predictor (ML Model)")
st.markdown("Fill in the details below to predict revenue:")

col1, col2, col3 = st.columns(3)
with col1:
    units = st.number_input("Units Sold", min_value=1, max_value=100, value=10)
    price = st.number_input("Unit Price (₹)", min_value=100, max_value=5000, value=1000)
    discount = st.slider("Discount", 0.0, 0.3, 0.1)
with col2:
    age = st.number_input("Customer Age", min_value=18, max_value=65, value=30)
    month = st.selectbox("Month", list(range(1,13)), index=0)
    day = st.selectbox("Day of Week (0=Mon)", list(range(7)), index=0)
with col3:
    category = st.selectbox("Category", df['Category'].unique())
    region = st.selectbox("Region", df['Region'].unique())
    gender = st.selectbox("Gender", ["Male", "Female"])

if st.button("🔮 Predict Revenue", use_container_width=True):
    try:
        base = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(base, '..', 'models', 'model.pkl')
        with open(model_path, 'rb') as f:
            model = pickle.load(f)

        from sklearn.preprocessing import LabelEncoder
        cat_map = {c: i for i, c in enumerate(sorted(df['Category'].unique()))}
        reg_map = {c: i for i, c in enumerate(sorted(df['Region'].unique()))}
        gen_map = {'Female': 0, 'Male': 1}

        input_data = np.array([[units, price, discount, age, month, day,
                                 cat_map[category], reg_map[region], gen_map[gender]]])
        prediction = model.predict(input_data)[0]
        st.success(f"💰 Predicted Revenue: ₹{prediction:,.2f}")
    except Exception as e:
        st.error(f"Error: {e}")

st.divider()
st.markdown("**Built with:** Python • Pandas • Scikit-learn • Streamlit • Matplotlib • Seaborn")
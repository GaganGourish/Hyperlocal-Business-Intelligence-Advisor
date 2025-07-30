import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import plotly.express as px

# Page Configuration
st.set_page_config(
    page_title="Cafe Review Analysis Dashboard",
    page_icon="☕",
    layout="wide"
)

# This function loads Manully created Datset and the analysed_data CSV and merges them.
@st.cache_data
def load_and_merge_data():
    try:
        analyzed_df = pd.read_csv('analyzed_reviews.csv')
        cafe_data_df = pd.read_csv('Cafe_Data.csv')
    except FileNotFoundError as e:
        st.error(f"Error: A required data file is missing. {e}")
        st.stop()

    # Join the two data tables using the URL columns.
    # Using a 'left' join to include all the rows from the reviews table.

    df = pd.merge(analyzed_df, cafe_data_df, left_on='Cafe_URL', right_on='Maps_URL', how='left')
    return df

df = load_and_merge_data()

# Main Page Title
st.title("Interactive Cafe Review Dashboard")
st.markdown("This dashboard provides an analysis of customer reviews for cafes in J.P. Nagar, Bangalore.")

st.sidebar.header("Filter Reviews")
unique_cafes = ['All Cafes'] + sorted(df['Cafe_Name'].unique().tolist())
selected_cafe = st.sidebar.selectbox("Select a Cafe", unique_cafes)

# Filtering by the Cafe Names
if selected_cafe == 'All Cafes':
    filtered_df = df
else:
    filtered_df = df[df['Cafe_Name'] == selected_cafe]

# Displaying the Key Metrics 
st.header(f"Analysis for: {selected_cafe}")
col1, col2, col3 = st.columns(3)
col1.metric("Total Reviews Analyzed", f"{filtered_df.shape[0]}")
col2.metric("Average Rating", f"{filtered_df['Rating'].mean():.2f} ⭐")
sentiment_counts = filtered_df['Sentiment_Label'].value_counts(normalize=True) * 100
positive_percentage = sentiment_counts.get('POSITIVE', 0)
col3.metric("Positive Sentiment", f"{positive_percentage:.1f}% 😊")

# Visualization
st.header("Visual Insights")

# Word Cloud Visualization
st.subheader("Most Common Words in Reviews")
text = ' '.join(filtered_df['Review_Text'].dropna())
if text:
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)
else:
    st.write("No review text available to generate a word cloud.")

# Bar Chart for Topic Distribution
st.subheader("Top Topics Discussed")
topic_counts = filtered_df['Topic'].value_counts().reset_index()
topic_counts.columns = ['Topic', 'Count']
topic_counts = topic_counts[topic_counts['Topic'] != -1]
if not topic_counts.empty:
    fig_topics = px.bar(topic_counts, x='Topic', y='Count', title="Frequency of Key Topics",
                        labels={'Topic': 'Topic Number', 'Count': 'Number of Reviews'})
    st.plotly_chart(fig_topics, use_container_width=True)
else:
    st.write("No topic data available for the selected cafe.")

st.header("Browse Individual Reviews")
st.dataframe(filtered_df[['Cafe_Name', 'Rating', 'Sentiment_Label', 'Review_Text']].dropna())
# Hyperlocal Business Intelligence Advisor

An NLP-powered web app that scrapes and analyzes customer reviews from Google Maps to provide actionable business intelligence for local cafes. This project transforms unstructured text into insights on customer sentiment and key business drivers.

-----

## Problem Statement

Small businesses, like local cafes, often lack the resources for dedicated market research teams. They have a wealth of valuable data in their public Google Maps reviews, but manually sifting through hundreds of comments to find meaningful patterns is impractical.

This project solves that problem by providing an automated tool that acts as a "Business Intelligence Advisor," answering critical questions:

  * What are our customers' main points of praise and complaint?
  * How do we compare to our local competitors?
  * What specific aspects of our business (e.g., service, food, ambiance) should we focus on improving?

-----

## Features

  * **Automated Review Scraping:** Uses Selenium to gather real-time review data from Google Maps.
  * **Advanced NLP Analysis:**
      * **Sentiment Analysis:** Classifies reviews as `POSITIVE` or `NEGATIVE` using a Hugging Face Transformer model.
      * **Topic Modeling:** Employs `BERTopic` to automatically discover key themes and topics discussed by customers.
  * **Interactive Dashboard:** A user-friendly Streamlit web application to visualize insights.
  * **Dockerized Application:** Fully containerized for easy deployment and portability.

-----

## Tech Stack

  * **Data Scraping:** Selenium
  * **Data Analysis:** Pandas, NumPy
  * **NLP:** Hugging Face (`transformers`), BERTopic, NLTK
  * **Web Framework:** Streamlit
  * **Containerization:** Docker
  * **Data Visualization:** Matplotlib, Plotly, WordCloud

-----

## Repository Structure

```
├── .dockerignore           # Specifies files to ignore in the Docker build
├── Dockerfile              # Blueprint for building the Docker image
├── requirements.txt        # List of all Python dependencies
├── app.py                  # The main Streamlit application script
├── Cafe_Data.csv           # Initial dataset with cafe names and URLs
├── Scraper.ipynb           # Notebook for scraping Google Maps reviews
├── data_cleaning.ipynb     # Notebook for text preprocessing and data cleaning
├── nlp_analysis.ipynb      # Notebook for sentiment and topic modeling analysis
└── *.csv                   # Intermediate and final datasets
```

-----

## How to Run

There are two ways to run this project: locally using the notebooks and Streamlit, or via Docker.

### 1\. Running Locally

**Prerequisites:** Python 3.11, Jupyter Notebook

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/hyperlocal_business_intelligence_advisor.git
    cd hyperlocal_business_intelligence_advisor
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Generate the data:**

      * Run the `Scraper.ipynb` notebook to generate `scraped_reviews.csv`.
      * Run the `data_cleaning.ipynb` notebook to generate `cleaned_reviews.csv`.
      * Run the `nlp_analysis.ipynb` notebook to generate the final `analyzed_reviews.csv`.

5.  **Launch the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

### 2\. Running with Docker (Recommended)

**Prerequisite:** Docker Desktop installed and running.

1.  **Clone the repository.**

2.  **Build the Docker image:**

    ```bash
    docker build -t cafe-analyzer-app .
    ```

3.  **Run the Docker container:**

    ```bash
    docker run -p 8501:8501 cafe-analyzer-app
    ```

4.  **Access the application** by navigating to `http://localhost:8501` in your web browser.

-----

## Project Workflow

The project follows a complete data science pipeline:

1.  **Data Acquisition:** The `Scraper.ipynb` notebook takes a list of cafe URLs from `Cafe_Data.csv` and scrapes their reviews.
2.  **Data Cleaning:** The `data_cleaning.ipynb` notebook cleans the raw text, handles missing values, and prepares it for analysis.
3.  **NLP Modeling:** The `nlp_analysis.ipynb` notebook applies sentiment analysis and topic modeling, creating the final `analyzed_reviews.csv`.
4.  **Presentation:** The `app.py` script loads the final dataset and presents the insights in an interactive web dashboard.

-----

## Author

  * **S.B. Gagan**

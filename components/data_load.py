import pandas as pd
from functools import lru_cache

# Dataset directory
DATASET_DIR = "https://raw.githubusercontent.com/Dashboard-Design/nyt-articles-dashboard/main/datasets/"

# List of parquet files hosted on GitHub
PARQUET_FILES = [
    "df_2015_2016.parquet",
    "df_2016_2018.parquet",
    "df_2018_2021.parquet",
    "df_2021_2024.parquet",
    "df_2024_2026.parquet"
]

@lru_cache(maxsize=1)  # cache the result of the function
def load_data():
    """
    Loads and caches NYT article datasets.
    - Reads all parquet files in datasets/
    - Creates a combined search_text column
    - Drops the original columns used for search_text
    - Reads the CSV for 'most viewed last 30 days'
    - Precomputes monthly trends for the entire dataset
    Returns:
        df (pd.DataFrame): Combined article data with search_text column
        df_most_viewed_l30 (pd.DataFrame): Last 30 days most viewed data
        monthly_trends (pd.DataFrame): Precomputed monthly article counts
    """
    # Collect all parquet files
    df = pd.concat(
        [pd.read_parquet(DATASET_DIR + file, engine="pyarrow") for file in PARQUET_FILES],
        ignore_index=True
    )
    
    # Columns to combine for search
    search_columns = ['keyword_one', 'keyword_two', 'keyword_three', 'keyword_four', 'headline', 'abstract']
    
    # Combine all parts with space separator for each row
    df['search_text'] = df[search_columns].fillna('').astype(str).apply(lambda x: ' '.join(x), axis=1)
    
    # Clean up extra spaces
    df['search_text'] = df['search_text'].str.replace(r'\s+', ' ', regex=True).str.strip().str.lower()
    
    # Drop the original columns that were used to create search_text
    df = df.drop(columns=search_columns)

    
    # Ensure published_date is datetime
    df['published_date'] = pd.to_datetime(df['published_date'], errors='coerce')
    df = df.dropna(subset=['published_date'])
    
    # Extract year and month for efficient grouping
    df['year'] = df['published_date'].dt.year
    df['month'] = df['published_date'].dt.month
    df['year_month'] = df['published_date'].dt.to_period('M') 


    # Precompute monthly trends for the entire dataset
    monthly_trends = df.groupby('year_month').size().reset_index(name='count')
    monthly_trends['year'] = monthly_trends['year_month'].dt.year
    monthly_trends['month'] = monthly_trends['year_month'].dt.month
    monthly_trends['date'] = monthly_trends['year_month'].dt.to_timestamp()   
        
        
    # Load CSV (cached because function is memoized)
    df_most_viewed_l30 = pd.read_csv(DATASET_DIR + "nyt_most_viewed_last30d.csv")

    return df, df_most_viewed_l30, monthly_trends

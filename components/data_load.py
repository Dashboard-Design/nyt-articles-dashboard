import glob
import pandas as pd
from pathlib import Path
from functools import lru_cache

# Dataset directory
DATASET_DIR = Path(__file__).parent.parent / "light dataset"
DATASET_DIR2 = Path(__file__).parent.parent / "datasets"

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
    parquet_files = glob.glob(str(DATASET_DIR / "*.parquet"))

    # Efficient concatenation with ignore_index=True
    df = pd.concat(
        [pd.read_parquet(file, engine="pyarrow") for file in parquet_files],
        ignore_index=True
    )

    # Ensure published_date is datetime
    df['published_date'] = pd.to_datetime(df['published_date'], errors='coerce')
    
    # Extract year and month for efficient grouping
    df['year'] = df['published_date'].dt.year
    df['year_month'] = df['published_date'].dt.to_period('M') 


    # Precompute monthly trends for the entire dataset
    monthly_trends = df.groupby('year_month').size().reset_index(name='count')
    monthly_trends['year'] = monthly_trends['year_month'].dt.year
    monthly_trends['month'] = monthly_trends['year_month'].dt.month
    monthly_trends['date'] = monthly_trends['year_month'].dt.to_timestamp()   
        
        
    # Load CSV (cached because function is memoized)
    df_most_viewed_l30 = pd.read_csv(DATASET_DIR2 / "nyt_most_viewed_last30d.csv")

    return df, df_most_viewed_l30, monthly_trends

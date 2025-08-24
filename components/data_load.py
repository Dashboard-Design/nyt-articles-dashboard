import glob
import pandas as pd
from pathlib import Path
from functools import lru_cache

# Dataset directory
DATASET_DIR = Path(__file__).parent.parent / "datasets"

@lru_cache(maxsize=1)  # cache the result of the function
def load_data():
    """
    Loads and caches NYT article datasets.
    - Reads all parquet files in datasets/
    - Creates a combined search_text column
    - Drops the original columns used for search_text
    - Reads the CSV for 'most viewed last 30 days'
    Returns:
        df (pd.DataFrame): Combined article data with search_text column
        df_most_viewed_l30 (pd.DataFrame): Last 30 days most viewed data
    """
    # Collect all parquet files
    parquet_files = glob.glob(str(DATASET_DIR / "*.parquet"))

    # Efficient concatenation with ignore_index=True
    df = pd.concat(
        [pd.read_parquet(file, engine="pyarrow") for file in parquet_files],
        ignore_index=True
    )
    
    # Columns to combine for search
    search_columns = ['keyword_one', 'keyword_two', 'keyword_three', 'keyword_four', 'headline', 'abstract']
    
    # Create search_text column by combining specified columns
    # Handle NaN values by converting to empty strings
    search_parts = []
    for col in search_columns:
        search_parts.append(df[col].fillna('').astype(str))
    
    if search_parts:
        # Combine all parts with space separator for each row
        df['search_text'] = df[search_columns].fillna('').astype(str).apply(lambda x: ' '.join(x), axis=1)
        
        # Clean up extra spaces
        df['search_text'] = df['search_text'].str.replace(r'\s+', ' ', regex=True).str.strip()
        
        # Drop the original columns that were used to create search_text
        existing_search_cols = [col for col in search_columns if col in df.columns]
        df = df.drop(columns=existing_search_cols)
        
        print(f"Created search_text column from: {existing_search_cols}")
        print(f"Dropped columns: {existing_search_cols}")
        
    # Load CSV (cached because function is memoized)
    df_most_viewed_l30 = pd.read_csv(DATASET_DIR / "nyt_most_viewed_last30d.csv")

    return df, df_most_viewed_l30
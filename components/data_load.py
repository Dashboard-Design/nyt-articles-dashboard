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
    - Reads the CSV for 'most viewed last 30 days'
    Returns:
        df (pd.DataFrame): Combined article data
        df_most_viewed_l30 (pd.DataFrame): Last 30 days most viewed data
    """
    # Collect all parquet files
    parquet_files = glob.glob(str(DATASET_DIR / "*.parquet"))

    # Efficient concatenation with ignore_index=True
    df = pd.concat(
        [pd.read_parquet(file, engine="pyarrow") for file in parquet_files]
    )

    # Load CSV (cached because function is memoized)
    df_most_viewed_l30 = pd.read_csv(DATASET_DIR / "nyt_most_viewed_last30d.csv")

    return df, df_most_viewed_l30

import requests
import time
import pandas as pd
from datetime import datetime

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # Add parent folder to path


import os
api_key = os.getenv("NYT_API_KEY")

last_days = 30

url = f"https://api.nytimes.com/svc/mostpopular/v2/viewed/{last_days}.json?api-key={api_key}"

response = requests.get(url)

# Safely check statusa
if response.status_code == 200:
    Data = response.json()
    print(f"Success: {Data['num_results']} results")
else:
    print("Failed:", response.status_code, response.text)


def processing_most_viewd_articles(article):
    result = {}
    result["id"] = article["id"]
    result["web_url"] = article["url"]
    result["abstract"] = article["abstract"]
    result["title"] = article["title"]

    result["keyword_one"] = None
    result["keyword_two"] = None
    result["keyword_three"] = None
    result["keyword_four"] = None
    result["keyword_five"] = None
    
    for i in range(min(5, len(article["des_facet"]))):
        result[f"keyword_{['one','two','three','four', 'five'][i]}"] = article["des_facet"][i]
    
    result["published_date"] = article["published_date"]
    result["section_name"] = article["section"]
    result["subsection"] = article["subsection"]
    result["image"] = article["media"][0]["media-metadata"][2]["url"]

    return result


nyt_most_viewed_last30d = []

for article in Data['results']:
    nyt_most_viewed_last30d.append(processing_most_viewd_articles(article))


output_path = f"{Path(__file__).parent.parent}/datasets/nyt_most_viewed_last30d.csv"

pd.DataFrame(nyt_most_viewed_last30d).to_csv(output_path, index=False)

print(f"✅ Exported successfully, {len(nyt_most_viewed_last30d)} articles.")
nyt_most_viewed_last30d.clear()     
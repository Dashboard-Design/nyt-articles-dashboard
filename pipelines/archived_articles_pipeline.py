import requests
import time
import pandas as pd
from datetime import datetime

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # Add parent folder to path


import os
api_key = os.getenv("NYT_API_KEY")


def processing_articles(article):
    result = {}
    result["id"] = article["_id"].split("/")[-1]
    result["web_url"] = article["web_url"]
    result["abstract"] = article["abstract"]
    result["lead_paragraph"] = article["lead_paragraph"]
    
    result["headline"] = article["headline"]["main"]
    
    result["keyword_one"] = None
    result["keyword_two"] = None
    result["keyword_three"] = None
    result["keyword_four"] = None

    result["published_date"] = article["pub_date"]
    result["news_desk"] = article["news_desk"]
    result["section_name"] = article["section_name"]
    if article.get("subsection_name" , 0) == 0:
        result["subsection_name"] = None
    else:    
        result["subsection_name"] = article["subsection_name"]
    result["word_count"] = article["word_count"]

    for i in range(min(4, len(article["keywords"]))):
        result[f"keyword_{['one','two','three','four'][i]}"] = article["keywords"][i]["value"]

    return result
        

end_year = datetime.now().year
end_month = datetime.now().month 

if end_month <= 4 :
    end_year -= 1
    end_month = (end_month - 4) + 12
else:
    end_year = end_year
    end_month = datetime.now().month - 4

print(end_year, end_month)            


output_path = f"{Path(__file__).parent.parent}/light dataset/df_2021_2026.parquet"

nyt_articles = []

if datetime.now().day == 1:
    url = f"https://api.nytimes.com/svc/archive/v1/{end_year}/{end_month}.json?api-key={api_key}"
    
    try:
        response = requests.get(url, timeout =60)

        if response.status_code == 429:
            print("Rate limit hit. Sleeping for 60 seconds...")
            time.sleep(60)
            
        elif response.status_code != 200:
            print(f"Failed {response.status_code}: {response.text}")
            time.sleep(20)
                
        Data = response.json()
        for article in Data['response']['docs']:
            nyt_articles.append(processing_articles(article))
            
        print(f"✅ Fetched {end_year}-{end_month:02d}. Sleeping for 5 seconds.")

        df = pd.DataFrame(nyt_articles)

        # Columns to combine for search
        search_columns = ['keyword_one', 'keyword_two', 'keyword_three', 'keyword_four', 'headline', 'abstract',  'news_desk',  'section_name', 'subsection_name']

        # Combine all parts with space separator for each row
        df['search_text'] = df[search_columns].fillna('').astype(str).apply(lambda x: ' '.join(x), axis=1)

        # Clean up extra spaces
        df['search_text'] = df['search_text'].str.replace(r'\s+', ' ', regex=True).str.strip().str.lower()

        # Drop the original columns that were used to create search_text
        df.drop(columns=search_columns, inplace=True)

        df_all = pd.concat( [pd.read_parquet(output_path) , df], ignore_index=True)

        df_all['published_date'] = pd.to_datetime(df['published_date'], errors='coerce')


    except requests.exceptions.SSLError as e:
        print(f"🔒 SSL Error on {end_year}-{end_month:02d}. Retrying after 30 seconds.")
        time.sleep(30)
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        time.sleep(30)
    
    df.to_parquet(output_path, index=False)

    nyt_articles.clear()   

else:
    print("It's not first day of the month to run this pipeline!")
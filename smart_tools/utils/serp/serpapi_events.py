import requests
import json
import pandas as pd
import os



def search_events(queries, api_key = os.environ['SERP_API_KEY']):
    serpapi_config = {
        "url": f"https://serpapi.com/search?no_cache=true&engine=google_events&api_key={api_key}",
        "headers": {
            'Content-Type': 'application/json',
            'Cache-Control': 'no-cache, max-age=0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
    }

    def search(query):
        # https://serpapi.com/google-events-api
        data = json.dumps(query)
        response = requests.request("GET", **serpapi_config, data=data)

        return response

    # print(queries)

    all_dfs = None

    for query in queries:
        print(rf"Processing `{query}`...")

        response = search(query)
        # print(response.text)
        events = json.loads(response.text)

        if "events_results" in events:
            e = events["events_results"]
            df = pd.DataFrame(events["events_results"])

            df['query'] = json.dumps(query)

            if all_dfs is None:
                all_dfs = df
            else:
                all_dfs = pd.concat([all_dfs, df])
        else:
            "  No events"

    if all_dfs is not None:
        all_dfs = all_dfs.copy()
        all_dfs = all_dfs.reset_index()
        all_dfs = all_dfs[['query', 'title', 'date', 'address', 'link']]
        return all_dfs


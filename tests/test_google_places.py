import pandas as pd
from smart_tools.utils.google import google_maps
from io import StringIO
import json
from datetime import datetime
import argparse

def process_queries(places, context, townships, elements, **kwargs):
    for place in places:
        all_dfs = None
        queries = [rf"{place} {context} {township}" for township in townships]

        for query in queries:
            print(rf"Processing `{query}`...")
            results = google_maps.search_by_places(query)

            df = pd.read_json(StringIO(json.dumps(results)))

            df['query'] = query

            if all_dfs is None:
                all_dfs = df
            else:
                all_dfs = pd.concat([all_dfs, df])

    if all_dfs is not None:

        all_dfs = all_dfs[elements]

        # all_dfs = all_dfs.copy()

        now = datetime.now()
        file_name = rf"C:\temp\places-{place}-{now.strftime('%Y%m%d%H%M%S')}.csv"
        file_name = rf"C:\temp\places-{place}.csv"
        all_dfs.to_csv(file_name, index=False)
        print(rf"Created {file_name}.")
        # all_dfs.drop_duplicates().to_csv(rf"C:\temp\{place}-{now.strftime('%Y%m%d%H%M%S')}-concise.csv", index=False)
    else:
        print("  no rows.")

    return file_name

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=str, help="Configuration file")

    args = parser.parse_args()

    with open(args.config, 'r') as file:
        CONFIG = json.load(file)

    return process_queries(**CONFIG)

if __name__ == "__main__":
    main()

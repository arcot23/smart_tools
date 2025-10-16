from smart_tools.utils.serp.serpapi_events import search_events
from datetime import datetime
import argparse
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=str, help="Configuration file")

    args = parser.parse_args()

    with open(args.config, 'r') as file:
        CONFIG = json.load(file)

    queries = [{"q": rf"{place} in {township}", "htichips": date} for date in CONFIG["dates"] for township in
               CONFIG["townships"] for place in
               CONFIG["places"]]

    all_dfs = search_events(queries)

    print(all_dfs.shape)

    if all_dfs is not None:
        now = datetime.now()
        file_name = rf"C:\temp\events-{CONFIG['title']}-{now.strftime('%Y%m%d%H%M%S')}.csv"
        file_name = rf"C:\temp\events-{CONFIG['title']}.csv"
        all_dfs.to_csv(file_name, index=False)

if __name__ == "__main__":
    main()

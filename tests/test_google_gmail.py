from smart_tools.utils.google import gmail_sender as gs, google_forms as gf
import pandas as pd
import json
import ast
import markdown
import argparse
from pathlib import Path

def process_file(file, CONFIG):
    print(rf"Reading `{file}`... ")

    df = pd.read_csv(file)

    for json_column in CONFIG["json_columns"]:
        df[json_column] = df[json_column].apply(json.loads)
        json_df = pd.json_normalize(df[json_column])
        new_df = pd.concat([df.drop(columns=[json_column]), json_df], axis=1)
        df = new_df

    for dict_column in CONFIG["dict_columns"]:
        print(dict_column)
        df[dict_column] = df[dict_column].apply(ast.literal_eval)
        json_df = df[dict_column].apply(pd.Series)
        new_df = pd.concat([df.drop(columns=[dict_column]), json_df], axis=1)
        df = new_df

    for list_column in CONFIG["list_columns"]:
        print(list_column)
        df[list_column['from']] = df[list_column['from']].apply(ast.literal_eval)
        split_df = pd.DataFrame(df[list_column['from']].tolist(), index=df.index, columns=list_column['to'])

        new_df = pd.concat([df, split_df], axis=1)
        df = new_df

    # print (df)
    # print(df.columns)

    if CONFIG["interesting_columns"] != []: df = df[CONFIG["interesting_columns"]]

    def print_row(r):
        # response = rf"""{r['when']}: [{r['title']}]({r['link']})  at {r['address']}\n"""
        # response = eval(params["output"])
        response = CONFIG["output"].format(**r.to_dict())
        # print(response)

        return response
        # for idx, c in r.items():
        #     print(c)
        # print()

    def df_to_markdown(df):
        s = df.apply(print_row, axis=1)
        bullets = s.str.cat(sep="\n")
        md_text = f"{CONFIG['email']['subject']}({df.shape[0]} records):\n\n{bullets}\n\n--\nAutomatically generated"
        return markdown.markdown(md_text)

    html = df_to_markdown(df)

    # with open(rf"C:\temp\events-20250926210247.html", "w") as f:
    #     f.write(html)
    # print(html)


    gs.send_email(sender=CONFIG["email"]["sender"],
                  to=CONFIG["email"]["receiver"] or gf.get_form_respondents_emails(CONFIG["email"]["emails_from_form_id"]),
                  subject=CONFIG["email"]["subject"] or Path(CONFIG["input_file"]).stem,
                  message_text=html,
                  email_type="html")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, help="Input file")
    parser.add_argument("config", type=str, help="Configuration file")

    args = parser.parse_args()

    with open(args.config, 'r') as file:
        CONFIG = json.load(file)

    process_file(args.file, CONFIG)

if __name__ == "__main__":
    main()

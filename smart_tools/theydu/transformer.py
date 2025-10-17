import csv
import json
import argparse
import os
from pathlib import Path

# csv_dynamic_transformer.py
import csv
import json

def transform_csv(input_csv: str, delimiter: str, config: str):
    """
    Reads an input CSV, applies dynamic field transformations using a JSON config,
    and writes a new CSV file with only the configured fields.

    :param input_csv: Path to input CSV file.
    :param config_json: Path to JSON config file defining new fields and templates.
    :param output_csv: Path to output CSV file to be created.
    """

    input_file_path = Path(input_csv)
    output_csv = f"{input_file_path.stem}_transformed.txt"
    output_csv = input_file_path.parent  / output_csv

    with open(input_csv, 'r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile, delimiter = delimiter)

        # Output columns = keys of config
        output_fields = list(config.keys())

        with open(output_csv, 'w', encoding='utf-8', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=output_fields)
            writer.writeheader()

            for row in reader:
                transformed_row = {}
                for key, template in config.items():
                    try:
                        transformed_row[key] = template.format(**row)
                    except KeyError as e:
                        transformed_row[key] = f"[Missing field: {e.args[0]}]"
                writer.writerow(transformed_row)



if __name__ == "__main__":
    config_path = r".\theydu_config\20251007-FULL-1_0_config.json"
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    path = config["file"]
    transform_config = config["transformation"]
    delimiter = config["delimiter"]
    print(f'File: {path}; Config: {transform_config}')

    transform_csv(path, delimiter, transform_config)


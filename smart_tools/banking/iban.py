import re
import yaml

import pandas as pd
import requests
import os

from smart_tools.banking.swift import regex_patterns as rp


def is_iban(text):
    pattern = f"^{rp.IBAN}$"

    return bool(re.match(pattern, text))


def parse(text):
    if not is_iban(text): raise ValueError("Invalid text. Expected IBAN.")
    pattern = f"^{rp.IBAN}$"
    countryCode = re.match(pattern, text).group(1)
    checkDigits = re.match(pattern, text).group(2)
    bban = re.match(pattern, text).group(3)

    return {'text': text, 'country_code': countryCode, 'check_digits': checkDigits, 'bban': bban}


def is_truly_iban(text):
    return


def download_iban_registry(
        url=yaml.load(open('.\config\iban_config.yaml'), Loader=yaml.SafeLoader)['iban_remote_registry_url'],
        local_path=yaml.load(open('.\config\iban_config.yaml'), Loader=yaml.SafeLoader)['iban_local_registry_file']):
    response = requests.get(url)
    with open(local_path, 'wb') as file:
        file.write(response.content)


def get_iban_lengths_from_registry(
        local_path=yaml.load(open('.\config\iban_config.yaml'), Loader=yaml.SafeLoader)['iban_local_registry_file']):
    if not os.path.exists(local_path):
        download_iban_registry()
    df = pd.read_csv(local_path, sep='\t', keep_default_na=False, skiprows=0, skipfooter=0, engine='python',
                     encoding='ansi',
                     quotechar='"', on_bad_lines='warn', dtype=str)
    df = df.transpose()
    df.columns = df.iloc[0]
    df = df.reset_index(drop=True).drop(0)
    return df


def write_iban_lengths_to_file(
        file=yaml.load(open('.\config\iban_config.yaml'), Loader=yaml.SafeLoader)['iban_local_length_file']):
    df = get_iban_lengths_from_registry()
    df.to_csv(file, index=False)


# print(get_iban_lengths())
write_iban_lengths_to_file()

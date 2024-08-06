import re
from smart_tools.banking.swift import regex_patterns as rp


def is_bic(text):
    pattern = f"^{rp.BIC}$"

    return bool(re.match(pattern, text))


def parse(text):
    if not is_bic(text): raise ValueError("Invalid text. Expected BIC.")
    pattern = f"^{rp.BIC}$"
    bankCode = re.match(pattern, text).group(1)
    countryCode = re.match(pattern, text).group(2)
    locationCode = re.match(pattern, text).group(3)
    branchCode = re.match(pattern, text).group(4)

    return {'text': text, 'bank_code': bankCode, 'country_code': countryCode, 'location_code': locationCode,
            'branch_code': branchCode}


def is_truly_bic(text):
    return

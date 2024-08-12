import re
import warnings
from smart_tools.banking.swift import regex_patterns as rp
from smart_tools.banking import bic
from smart_tools.banking import iban


def is_valid(text, option, line_sep=' _ '):
    warnings.warn("Function is_valid() not implemented.")
    # replaced_sep = "#"
    # text = text.replace(line_sep, replaced_sep)
    # if option not in ['A', 'B', 'D', 'F', 'K', '']: ValueError("Invalid `option`. Expected 'A', 'B', 'D', 'F', 'K' or ''.")
    # if option == 'A':
    #     matches = re.findall(f'^({rp.ACCT})({replaced_sep})?({rp.BIC})$', text)
    #     if matches: return True
    # elif option == 'F':
    #     matches = re.findall(rp.OPTIONF1, text)
    #     if matches: return True
    return False


def find_option(text, line_sep=" _ ", has_acct=True):
    warnings.warn("Function find_option() not implemented.")

    return


def parse(text, option=None, get_option=True, line_sep=' _ ', has_acct=True):
    def fetch_country(dict):
        country_dict = {'bic_country_code': None, 'optionf_country_code': None, 'iban_country_code': None}

        if response_dict['has_bic']:
            country_dict['bic_country_code'] = response_dict['bic']['country_code']

        if response_dict['option'] == 'F':
            for item in dict:
                if not dict[item] is None:
                    if re.search('line[1234]', item) and re.search('3\/(\w+)', dict[item]): country_dict[
                        'optionf_country_code'] = re.search('3\/(\w+)', dict[item]).group(1)

        if response_dict['has_iban']:
            country_dict['iban_country_code'] = response_dict['iban']['country_code']

        return country_dict

    response_dict = {'text': text, 'option': option, 'has_text': False, 'total_lines': None,
                     'has_acct': False, 'has_bic': False,
                     'has_iban': False, 'acct': None, 'line1': None, 'line2': None,
                     'line3': None, 'line4': None, 'bic': None,
                     'iban': None, 'name': None, 'country': None}

    if text is None: return response_dict

    if not get_option and option is None:
        raise TypeError("Expected `option` when `get_option` is False.")
    if option not in ['A', 'B', 'D', 'F', 'K', '']:
        raise ValueError("Invalid `option`. Expected 'A', 'B', 'D', 'F', 'K' or ''.")
    if get_option and option is not None:
        warnings.warn("Process will override `option`. To disable, set `get_option` to False.")

    if len(text.strip()) > 0: response_dict['has_text'] = True
    values = text.split(line_sep)
    line_start_index = 0

    ###########

    response_dict['total_lines'] = len(values)

    if text.startswith('/'):
        response_dict['acct'] = re.search(f'{rp.ACCT}', values[0]).group(1)
        response_dict['has_acct'] = True
        line_start_index = 1
    else:
        response_dict['name'] = values[0]

    for index, value in enumerate(range(line_start_index, len(values))):
        response_dict[f'line{index + 1}'] = values[value]

    if response_dict['option'] == 'A' and bic.is_bic(response_dict['line1']):
        response_dict['has_bic'] = True
        response_dict['bic'] = bic.parse(response_dict['line1'])

    if response_dict['has_acct'] and iban.is_iban(response_dict['acct']):
        response_dict['has_iban'] = True
        response_dict['iban'] = iban.parse(response_dict['acct'])

    response_dict['country'] = fetch_country(response_dict)

    return response_dict

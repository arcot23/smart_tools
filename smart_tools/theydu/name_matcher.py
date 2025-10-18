from pathlib import Path
import re
from difflib import SequenceMatcher
import jellyfish
# import pandas as pd
from fuzzywuzzy import fuzz
import json
import match_tools as mt

def match_names(s1:str, s2:str):
    """
    Match two names using different scenarios.

    This function calculates the similarity between two strings using various algorithms and returns a JSON response with the scores for each scenario.

    Parameters:

    s1 (str): The search string to be compared.
    s2 (str): The name string to be compared against.

    Returns:

    json_response (dict): A JSON response with the scores for all scenarios.

    Notes:
    The function uses the following algorithms to calculate the similarity between the two strings:

    - Exact Match
    - Levenshtein Distance
    - Jaro-Winkler Distance
    - Match Score without Any Char Removal
    - Match Score after Normalization
    - Match Score after Tokenization
    - FuzzyWuzzy Ratio
    - FuzzyWuzzy Partial Ratio
    - FuzzyWuzzy Token Sort Ratio
    - FuzzyWuzzy Token Set Ratio
    - FuzzyWuzzy QRatio
    - FuzzyWuzzy WRatio

    See Also:

    - `jellyfish` library for phonetic algorithms
    - `fuzzywuzzy` library for fuzzy matching algorithms
    - `difflib` library for sequence matching algorithms
    """
    s1_normalized = re.sub(r'[^a-z0-9]', '', s1.lower())
    s2_normalized = re.sub(r'[^a-z0-9]', '', s2.lower())

    # Initialize the response dictionary to store the results of each scenario
    response = {
        "s1": s1,
        "s2": s2,
        "length": {},  # Store the length of the strings
        "phonetic_encoding": {},  # Store the phonetic encodings of the strings
        "scores": {},  # Store the scores for each scenario
        "analysis":{}
    }

    """
    Calculate the length of the strings
    -------------------------------
    The length of the strings is calculated using the `len` function.
    """
    response["length"]["exact"] = [len(s1), len(s2)]
    """
    Calculate the length of the strings after removing non-alphanumeric characters
    ---------------------------------------------------------------
    The length of the strings is calculated after removing non-alphanumeric characters using the `re.sub` function.
    """
    response["length"]["normalized"] = [len(re.sub(r'[^a-z0-9]', '', s1)), len(re.sub(r'[^a-z0-9]', '', s2))]

    """
    Calculate the phonetic encodings of the strings
    -----------------------------------------
    The phonetic encodings of the strings are calculated using the `jellyfish` library.
    The following phonetic algorithms are used:
    - Soundex
    - Metaphone
    - NYSIIS
    - Match Rating Codex
    """
    response["phonetic_encoding"]["soundex"] = [jellyfish.soundex(s1), jellyfish.soundex(s2)]
    response["phonetic_encoding"]["metaphone"] = [jellyfish.metaphone(s1), jellyfish.metaphone(s2)]
    response["phonetic_encoding"]["nysiis"] = [jellyfish.nysiis(s1), jellyfish.nysiis(s2)]
    response["phonetic_encoding"]["match_rating_codex"] = [jellyfish.match_rating_codex(s1_normalized), jellyfish.match_rating_codex(s1_normalized)]

    response["analysis"]["longest_common_subsequence"] = mt.longest_common_subsequence(s1, s2)
    response["analysis"]["align_names"] = mt.align_names(s1, s2)
    response["analysis"]["align_names_lcs"] = mt.align_names_lcs(s1, s2)

    """
    Scenario 1: Exact Match
    ---------------------
    The exact match scenario checks if the search string and name string are identical (case-insensitive).
    The score is calculated as 1.0 if the strings are identical, and 0.0 otherwise.
    """
    response["scores"]["exact_match"] = 1.0 if s1.lower() == s2.lower() else 0.0

    """
    Scenario 2: Fuzzy Match (Levenshtein Distance)
    -----------------------------------------
    The Levenshtein distance scenario calculates the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other.
    The score is calculated as 1 minus the ratio of the Levenshtein distance to the maximum length.
    """

    distance = jellyfish.levenshtein_distance(s1.lower(), s2.lower())
    max_distance = max(len(s1), len(s2))
    response["scores"]["levenshtein_distance"] = 1.0 - (distance / max_distance)

    """
    Scenario 3: Fuzzy Match (Jaro-Winkler Distance)
    ------------------------------------------
    The Jaro-Winkler distance scenario calculates the similarity between two strings, giving more weight to prefix matches.
    The score is calculated using the `jellyfish.jaro_winkler_similarity` function.
    """
    response["scores"]["jaro_winkler_distance"] = jellyfish.jaro_winkler_similarity(s1.lower(), s2.lower())

    """
    Scenario 4: Match Score without Any Char Removal
    ---------------------------------------------
    The match score without any char removal scenario calculates the match score without removing any characters.
    The score is calculated as the ratio of matching characters to the maximum length.
    """
    s1_lower = s1.lower()
    s2_lower = s2.lower()
    matches = sum(1 for a, b in zip(s1_lower, s2_lower) if a == b)
    response["scores"]["match_score_without_removal"] = matches / max(len(s1), len(s2))

    """
    Scenario 5: Match Score after Normalization
    ---------------------------------------
    The match score after normalization scenario calculates the match score after normalizing the strings (removing non-alphanumeric characters).
    The score is calculated using the `SequenceMatcher.ratio` function.
    """
    response["scores"]["match_score_after_normalization"] = SequenceMatcher(None, s1_normalized, s2_normalized).ratio()

    """
    Scenario 6: Match Score after Tokenization
    --------------------------------------
    The match score after tokenization scenario calculates the match score after tokenizing the strings (splitting into words).
    The score is calculated as the ratio of matching tokens to the maximum number of tokens.
    """
    search_tokens = s1.lower().split()
    name_tokens = s2.lower().split()
    matches = sum(1 for token in search_tokens if token in name_tokens)
    response["scores"]["match_score_after_tokenization"] = matches / max(len(search_tokens), len(name_tokens))

    """
    Scenario 7: Fuzzy Match (FuzzyWuzzy Ratio)
    ---------------------------------------
    The FuzzyWuzzy ratio scenario calculates the similarity between two strings using the Levenshtein distance.
    The score is calculated using the `fuzz.ratio` function.
    """
    response["scores"]["fuzzywuzzy_ratio"] = fuzz.ratio(s1.lower(), s2.lower()) / 100

    """
    Scenario 8: Fuzzy Match (FuzzyWuzzy Partial Ratio)
    ----------------------------------------------
    The FuzzyWuzzy partial ratio scenario calculates the similarity between two strings using the Levenshtein distance, but only considering the shortest string.
    The score is calculated using the `fuzz.partial_ratio` function.
    """
    response["scores"]["fuzzywuzzy_partial_ratio"] = fuzz.partial_ratio(s1.lower(), s2.lower()) / 100

    """
    Scenario 9: Fuzzy Match (FuzzyWuzzy Token Sort Ratio)
    ------------------------------------------------
    The FuzzyWuzzy token sort ratio scenario calculates the similarity between two strings using the Levenshtein distance, but sorting the tokens before comparison.
    The score is calculated using the `fuzz.token_sort_ratio` function.
    """
    response["scores"]["fuzzywuzzy_token_sort_ratio"] = fuzz.token_sort_ratio(s1.lower(), s2.lower()) / 100

    """
    Scenario 10: Fuzzy Match (FuzzyWuzzy Token Set Ratio)
    --------------------------------------------------
    The FuzzyWuzzy token set ratio scenario calculates the similarity between two strings using the Levenshtein distance, but considering the set of tokens instead of their order.
    The score is calculated using the `fuzz.token_set_ratio` function.
    """
    response["scores"]["fuzzywuzzy_token_set_ratio"] = fuzz.token_set_ratio(s1.lower(), s2.lower()) / 100

    """
    Scenario 11: Fuzzy Match (FuzzyWuzzy QRatio)
    ----------------------------------------
    The FuzzyWuzzy QRatio scenario calculates the similarity between two strings using the Levenshtein distance, but considering the longest contiguous matching substring.
    The score is calculated using the `fuzz.QRatio` function.
    """
    response["scores"]["fuzzywuzzy_qratio"] = fuzz.QRatio(s1.lower(), s2.lower()) / 100

    """
    Scenario 12: Fuzzy Match (FuzzyWuzzy WRatio)
    ----------------------------------------
    The FuzzyWuzzy WRatio scenario calculates the similarity between two strings using the Levenshtein distance, but considering the weighted ratio of matching characters.
    The score is calculated using the `fuzz.WRatio` function.
    """
    response["scores"]["fuzzywuzzy_wratio"] = fuzz.WRatio(s1.lower(), s2.lower()) / 100

    # Scenario 13: Acronym Match
    def acronym_match(search_string, name_string):
        search_acronyms = re.findall(r'$$[A-Z]+$$', search_string)
        name_acronyms = re.findall(r'$$[A-Z]+$$', name_string)
        if search_acronyms and name_acronyms:
            return 1.0 if search_acronyms[0].strip('()') == name_acronyms[0].strip('()') else 0.0
        else:
            search_acronym = re.sub(r'[^A-Z]', '', search_string)
            name_acronym = re.sub(r'[^A-Z]', '', name_string)
            return 1.0 if search_acronym == name_acronym else 0.0

    response["scores"]["acronym_match"] = acronym_match(s1, s2)

    # Scenario 14: Jaccard Similarity
    response["scores"]["jaccard_similarity"] = mt.jaccard_similarity(s1, s2)

    # Scenario 15: Cosine Similarity
    response["scores"]["cosine_similarity"] = mt.cosine_similarity(s1, s2)

    # Return the response as a JSON string
    return json.dumps(response, indent=4)


def main():
    # Example usage:
    s1 = "prabhu ram prasath"
    s2 = "ram prasat"
    result = match_names(s1, s2)
    print(type(result))
    print(result)
    j = json.loads(result)
    highest_scorer = max(j["scores"], key=j["scores"].get)
    print(rf'Highest scorer for (`{s1}`, `{s2}`) is (`{highest_scorer}`: {j["scores"][highest_scorer]})')

# def match_names_in_csv(file):
#     input_file = file
#     output_file = rf"{Path(file).parent}\{Path(file).stem}_match_results.csv"
#     df = pd.read_csv(input_file)
#
#     df["match_results"] = df.apply(lambda r: match_names(r['s1'], r['s2']), axis = 1)
#
#     # df['json'] = df['match_results'].apply(json.loads)
#
#     def extract_highest_value(json_string):
#         data = json.loads(json_string)
#         scores = data['scores']
#         highest_value_key = max(scores, key=scores.get)
#         return highest_value_key, "{:.2f}".format(scores[highest_value_key])
#
#     def extract_ranked_value(json_string, rank=1):
#         """
#         Extracts the keys and value from the 'scores' dictionary in the JSON string
#         based on the specified rank.
#
#         Args:
#             json_string (str): The input JSON string.
#             rank (int): The rank of the value to be extracted (1-indexed).
#
#         Returns:
#             tuple: A tuple containing the list of keys and value at the specified rank.
#         """
#         data = json.loads(json_string)
#         scores = data['scores']
#         # sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
#         sorted_scores = sorted(set(scores.values()), reverse=True)
#         # print(sorted_scores)
#         if rank > len(sorted_scores):
#             return None, None
#         target_value = sorted_scores[rank - 1]
#         ranked_keys = [key for key, value in scores.items() if value == target_value]
#         return ranked_keys, "{:.2f}".format(target_value)
#
#     for i in range(1, 11):
#         df[[f'rank_{i}', f'score_{i}']] = df['match_results'].apply(lambda r: pd.Series(extract_ranked_value(r, i)))
#
#     # print(df)
#
#     df.to_csv(output_file, index=False)

if __name__ == "__main__":
    main()
    # match_names_in_csv("./data/test_names.csv")
import numpy as np
from collections import Counter
import re

def jaccard_similarity(s1, s2):
    """
    Calculates the Jaccard Similarity (or Jaccard Index) between two sets.

    The Jaccard Similarity is defined as the size of the intersection
    divided by the size of the union of the two sets.

    Args:
        s1 (set): The first set.
        s2 (set): The second set.

    Returns:
        float: The Jaccard Similarity score, a value between 0 and 1.
    """

    # Convert inputs to sets in case they are lists or other iterables
    set1 = set(s1)
    set2 = set(s2)

    # Calculate the intersection (common elements)
    intersection = set1.intersection(set2)

    # Calculate the union (all unique elements)
    union = set1.union(set2)

    # Jaccard Similarity = |Intersection| / |Union|
    if not union:
        # Handle the case where both sets are empty (similarity is often 1.0
        # or 0.0 depending on the specific application, 1.0 is common)
        return 1.0

    return len(intersection) / len(union)




def cosine_similarity_strings(s1: str, s2: str) -> float:
    """
    Calculates the cosine similarity between two strings based on their word-count vectors.

    Args:
        s1: The first string.
        s2: The second string.

    Returns:
        The cosine similarity score, a float between 0.0 and 1.0.
    """

    # 1. Tokenization and Normalization
    # Simple tokenization: lowercase, remove non-word characters, and split into words
    def get_tokens(text):
        text = text.lower()
        # Use regex to find all sequences of word characters (letters, numbers, underscore)
        return re.findall(r'\b\w+\b', text)

    tokens1 = get_tokens(s1)
    tokens2 = get_tokens(s2)

    if not tokens1 or not tokens2:
        return 0.0  # Return 0 if either string is empty

    # 2. Vectorization (Bag-of-Words model)
    # Create word-count dictionaries (vectors)
    count1 = Counter(tokens1)
    count2 = Counter(tokens2)

    # Get the union of all unique words from both strings
    all_words = set(count1.keys()) | set(count2.keys())

    # Create the full vectors (lists of word counts)
    v1 = np.array([count1.get(word, 0) for word in all_words])
    v2 = np.array([count2.get(word, 0) for word in all_words])

    # 3. Cosine Similarity Calculation

    # Dot product: sum(v1[i] * v2[i])
    dot_product = np.dot(v1, v2)

    # L2 Norm (Magnitude): sqrt(sum(v[i]^2))
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)

    norm_product = norm_v1 * norm_v2

    # Avoid division by zero (though handled by the initial check,
    # this is a final safeguard for the vector math)
    if norm_product == 0:
        return 0.0

    return dot_product / norm_product


def longest_common_subsequence(s1, s2):
    return 0

def align_names(s1, s2):
    return 0

def align_names_lcs(s1, s2):
    return 0
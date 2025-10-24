There are different ways to match two strings:

# Exact matching

For a definitive, character-for-character comparison, use one of these methods.

### Case-sensitive comparison: 

Most programming languages provide a built-in method (`==` in Python) that returns true only if the strings have the exact same sequence of characters.
`"cat" == "Cat"` returns `false`.

### Case-insensitive comparison

Many languages also offer a function to ignore case when comparing. For example, using `.casefold()` on both strings in Python.
`"Hello, World".casefold("hello, world")` returns `true`.

### Normalized comparison

If you need to ignore leading or trailing white space, you can trim the strings before comparing them. `" hello ".strip().equals("hello")` returns `true`.

| **Normalization Type**                   | **Purpose / Description**                                                    | **Python One-Liner Example**                                                                                                                 |
| ---------------------------------------- | ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Lowercasing**                          | Standardizes text by converting all characters to lowercase.                 | `text = text.lower()`                                                                                                                        |
| **Removing Punctuation**                 | Eliminates punctuation marks to simplify token comparison.                   | `import re; text = re.sub(r'[^\w\s]', '', text)`                                                                                             |
| **Removing Numbers**                     | Removes digits when they are not semantically meaningful.                    | `text = re.sub(r'\d+', '', text)`                                                                                                            |
| **Whitespace Normalization**             | Collapses multiple spaces or tabs into a single space.                       | `text = ' '.join(text.split())`                                                                                                              |
| **Accent / Diacritic Removal**           | Converts accented characters to ASCII equivalents.                           | `import unicodedata; text = ''.join(c for c in unicodedata.normalize('NFKD', text) if not unicodedata.combining(c))`                         |
| **Unicode Normalization**                | Ensures consistent Unicode representation (NFC/NFD).                         | `import unicodedata; text = unicodedata.normalize('NFC', text)`                                                                              |
| **Tokenization**                         | Splits text into individual words or tokens.                                 | `from nltk.tokenize import word_tokenize; tokens = word_tokenize(text)`                                                                      |
| **Stopword Removal**                     | Removes common words (e.g., “the”, “is”) to reduce noise.                    | `from nltk.corpus import stopwords; text = ' '.join([w for w in text.split() if w not in stopwords.words('english')])`                       |
| **Lemmatization**                        | Converts words to their base (dictionary) form using POS context.            | `from nltk.stem import WordNetLemmatizer; lemmatizer = WordNetLemmatizer(); text = ' '.join([lemmatizer.lemmatize(w) for w in text.split()])` |
| **Stemming**                             | Truncates words to their root form (may be less precise than lemmatization). | `from nltk.stem import PorterStemmer; stemmer = PorterStemmer(); text = ' '.join([stemmer.stem(w) for w in text.split()])`                   |
| **Expanding Contractions**               | Converts contractions to full forms (e.g., “don’t” → “do not”).              | `import contractions; text = contractions.fix(text)`                                                                                         |
| **Removing Special Characters / Emojis** | Strips out non-textual characters or emojis.                                 | `text = re.sub(r'[^\x00-\x7F]+', '', text)`                                                                                                  |
| **Spelling Correction**                  | Fixes common spelling errors.                                                | `from textblob import TextBlob; text = str(TextBlob(text).correct())`                                                                        |
| **URL / Email Removal**                  | Removes URLs and email addresses from text.                                  | `text = re.sub(r'http\S+', '', text)`                                                                                                                     |
| **Case Folding (Aggressive)**            | Handles locale-insensitive case mapping beyond lower().                      | `text = text.casefold()`                                                                                                                     |
| **Removing HTML Tags**                   | Cleans text scraped from web sources.                                        | `from bs4 import BeautifulSoup; text = BeautifulSoup(text, 'html.parser').get_text()`                                                        |
| **Synonym Replacement (Optional)**       | Replaces words with synonyms for standardization.                            | `from nltk.corpus import wordnet; synonyms = [wordnet.synsets(w)[0].lemmas()[0].name() if wordnet.synsets(w) else w for w in text.split()]`  |


# Approximate or "fuzzy" matching

If you need to find how similar two strings are, fuzzy matching algorithms provide a numerical score, or "distance," rather than a simple true/false answer. 

## Edit distance-based algorithms

These metrics calculate the minimum number of single-character edits required to change one string into the other. 

### Levenshtein distance: 

The standard edit distance metric, which counts the number of insertions, deletions, and substitutions needed to make two strings identical. A lower number indicates a higher similarity.
Distance between "kitten" and "sitting" is 3.

| **Method**                                       | **Description**                                               | **Python One-/Two-Liner Example**                                                                                                                                   |
| ------------------------------------------------ | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Using `python-Levenshtein` library (fastest)** | C-optimized implementation; ideal for production.             | `import Levenshtein; dist = Levenshtein.distance("kitten", "sitting")`                                                                                              |
| **Using `textdistance` library**                 | Pure Python alternative supporting multiple distance metrics. | `import textdistance; dist = textdistance.levenshtein("kitten", "sitting")`                                                                                         |
| **Using `difflib` (standard library)**           | Not exact Levenshtein but gives a close similarity ratio.     | `import difflib; dist = 1 - difflib.SequenceMatcher(None, "kitten", "sitting").ratio()`                                                                             |
| **Manual Dynamic Programming (no libraries)**    | Demonstrates the logic behind Levenshtein distance.           | `dist = lambda a,b: (len(a) and len(b) and min(dist(a[1:],b[1:])+ (a[0]!=b[0]), dist(a[1:],b)+1, dist(a,b[1:])+1)) or abs(len(a)-len(b)); dist("kitten","sitting")` |


### Damerau-Levenshtein distance: 

An extension of the Levenshtein distance that includes transpositions (swapping two adjacent characters) as an additional edit operation. It is often a better measure for human typographical errors.
Distance between "from" and "form" is 1 using this algorithm, but 2 using Levenshtein.

| **Method**                                            | **Description**                                                       | **Python One-/Two-Liner Example**                                                                                                                                                                                                                                         |
| ----------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Using `textdistance` library**                      | Easiest pure-Python implementation (supports transpositions).         | `import textdistance; dist = textdistance.damerau_levenshtein("ca", "abc")`                                                                                                                                                                                               |
| **Using `pyxdameraulevenshtein` library (optimized)** | Fast C-extension version suitable for high-volume text comparison.    | `from pyxdameraulevenshtein import damerau_levenshtein_distance as dld; dist = dld("ca", "abc")`                                                                                                                                                                          |
| **Using `jellyfish` library**                         | Lightweight string-similarity toolkit (includes Damerau-Levenshtein). | `import jellyfish; dist = jellyfish.damerau_levenshtein_distance("ca", "abc")`                                                                                                                                                                                            |
| **Manual DP (recursive demo – not optimized)**        | Educational demonstration using recursion.                            | `dist = lambda a,b: (len(a) and len(b) and min(dist(a[1:],b[1:])+ (a[0]!=b[0]), dist(a[1:],b)+1, dist(a,b[1:])+1, dist(a[1:],b[1:])+ (a[0]!=b[1] or a[1]!=b[0]) if len(a)>1 and len(b)>1 and a[0]==b[1] and a[1]==b[0] else 99)) or abs(len(a)-len(b)); dist("ca","abc")` |


## Token-based algorithms

These methods treat strings as collections of "tokens," such as individual words or character sequences (n-grams), to measure their overlap. 

### Jaccard similarity

Measures the similarity between two sets by dividing the size of their intersection by the size of their union. For strings, you can first tokenize them into sets of words or n-grams.

`s1 = "the quick brown fox"` -> `{"the", "quick", "brown", "fox"}`

`s2 = "a quick brown dog"` -> `{"a", "quick", "brown", "dog"}`

`s1 ∪ s2` -> `{"quick", "brown"}`

`s1 ∩ s2` ->  `{"the", "quick", "brown", "fox", "a", "dog"}`

Jaccard score -> `|2|/|6|` -> `0.33`

| **Method**                                      | **Description**                                                 | **Python One-/Two-Liner Example**                                                                      |     |
| ----------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | --- |
| **Using Python sets (manual)**                  | Fastest and simplest method for token-based Jaccard similarity. | `a, b = set("night"), set("nacht"); sim = len(a & b) / len(a                                           | b)` |
| **Using `textdistance` library**                | Provides robust similarity metrics including Jaccard.           | `import textdistance; sim = textdistance.jaccard("night", "nacht")`                                    |     |
| **Using `sklearn` (for binary vectors)**        | Ideal for comparing binary feature vectors.                     | `from sklearn.metrics import jaccard_score; sim = jaccard_score([1,1,0,1],[1,0,1,1])`                  |     |
| **Token-based Jaccard (with whitespace split)** | Computes Jaccard over words instead of characters.              | `a,b = set("the cat sleeps".split()), set("the cat eats".split()); sim = len(a & b) / len(a            | b)` |
| **Using `nltk` n-grams**                        | Jaccard similarity over n-gram tokens.                          | `from nltk import ngrams; a,b = set(ngrams("night",2)), set(ngrams("nacht",2)); sim = len(a & b)/len(a | b)` |


### Cosine similarity

Represents strings as vectors (e.g., using TF-IDF), then measures the cosine of the angle between them. A value closer to 1 indicates higher similarity. This is particularly useful for longer documents.

| **Method**                                      | **Description**                                            | **Python One-/Two-Liner Example**                                                                                                                                                 |
| ----------------------------------------------- | ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Using `sklearn` (vector-based)**              | Standard method for comparing numeric or TF-IDF vectors.   | `from sklearn.metrics.pairwise import cosine_similarity; sim = cosine_similarity([[1,2,3]], [[2,4,6]])[0][0]`                                                                     |
| **Manual NumPy computation**                    | Lightweight and dependency-free for numeric vectors.       | `import numpy as np; a,b = np.array([1,2,3]), np.array([2,4,6]); sim = np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))`                                                         |
| **Using `textdistance` library (string-based)** | Approximation for text strings (works at character level). | `import textdistance; sim = textdistance.cosine("night", "nacht")`                                                                                                                |
| **TF-IDF with `sklearn`**                       | Ideal for sentence/document similarity in NLP.             | `from sklearn.feature_extraction.text import TfidfVectorizer; v = TfidfVectorizer().fit_transform(["dog bites man", "man bites dog"]); sim = cosine_similarity(v[0], v[1])[0][0]` |
| **Using `scipy`**                               | Direct cosine distance → similarity conversion.            | `from scipy.spatial.distance import cosine; sim = 1 - cosine([1,2,3],[2,4,6])`                                                                                                    |

There are other similarity algorithms like Euclidean, Manhattan, and Hamming similarity/distance.

# Hybrid and phonetic algorithms

These approaches combine or use different strategies for specialized matching tasks. 

### Jaro-Winkler similarity

Favors strings that share a common prefix, making it well-suited for names and other data where misspellings often occur toward the end of a string.

| **Method**                                             | **Description**                                                        | **Python One-/Two-Liner Example**                                                                        |
| ------------------------------------------------------ | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Using `jellyfish` (most common)**                    | Efficient and reliable C-based Jaro–Winkler similarity implementation. | `import jellyfish; sim = jellyfish.jaro_winkler_similarity("martha", "marhta")`                          |
| **Using `textdistance` library**                       | Pure Python implementation, easier for experimentation.                | `import textdistance; sim = textdistance.jaro_winkler("martha", "marhta")`                               |
| **Using `pyjarowinkler` library**                      | Dedicated library for accurate name-matching scenarios.                | `from pyjarowinkler import distance; sim = distance.get_jaro_distance("martha", "marhta", winkler=True)` |
| **Manual fallback using Jaro only (no Winkler boost)** | Simpler variant if Winkler weighting not required.                     | `sim = textdistance.jaro("martha", "marhta")`                                                            |


### Phonetic algorithms

Translate words into a phonetic representation (e.g., a Soundex code) and compare those instead of the original strings. This is effective for matching words that sound similar but are spelled differently. 

| **Algorithm**                          | **Purpose / Description**                                                    | **Python One-/Two-Liner Example**                                             |
| -------------------------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Soundex (`jellyfish`)**              | Encodes words by English pronunciation (for deduplication, genealogy, etc.). | `import jellyfish; code = jellyfish.soundex("Robert")`                        |
| **Metaphone (`jellyfish`)**            | Improved over Soundex, handles more phonetic edge cases.                     | `code = jellyfish.metaphone("Robert")`                                        |
| **NYSIIS (`jellyfish`)**               | Normalizes phonemes for US names; more linguistically robust.                | `code = jellyfish.nysiis("Robert")`                                           |
| **Match Rating Codex (`jellyfish`)**   | Designed for name matching; good for record linkage.                         | `code = jellyfish.match_rating_codex("Robert")`                               |
| **Double Metaphone (`fuzzy` library)** | Returns two encodings (primary/secondary) for ambiguous sounds.              | `from fuzzy import DMetaphone; dmeta = DMetaphone(); codes = dmeta("Robert")` |

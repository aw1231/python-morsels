from typing import Dict


def count_words(input: str) -> Dict[str, int]:
    in_split = input.split()
    dict: Dict[str, int] = {}
    for word in in_split:
        word_normalized = word.lower()
        if word_normalized in dict:
            dict[word_normalized] = dict[word_normalized] + 1
        else:
            dict[word_normalized] = 1
    return dict

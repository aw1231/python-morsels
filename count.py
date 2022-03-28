def count_words(input: str) -> dict:
    in_split = input.split()
    dict = {}
    for word in in_split:
        word_normalized = word.lower()
        if word_normalized in dict:
            dict[word_normalized] = dict[word_normalized] + 1
        else:
            dict[word_normalized] = 1
    return dict
import string

def word_filter_counter(text, filter_words):
    text_clean = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words_list = text_clean.split()
    count = {}
    for word in words_list:
        if word in filter_words:
            if word in count:
                count[word] +=1
            else:
                count[word] = 1

    return count

print(
    word_filter_counter("Hello world, hello!", ["hello"])
)
print(
    word_filter_counter("The quick brown fox.", ["the"])
)  # Expected output: {'the': 1}
print(
    word_filter_counter(
        "Is this real life? Is this just fantasy?", ["is", "this", "just"]
    )
)  # Expected output: {'is': 2, 'this': 2, 'just': 1}
print(
    word_filter_counter(
        "Do we see the big picture or just small details?", ["we", "the", "or"]
    )
)  # Expected output: {'we': 1, 'the': 1, 'or': 1}


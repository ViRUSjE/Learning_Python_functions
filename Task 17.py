a  = ['Litwo', 'ojcyzno', 'moja', 'ty', 'jestes', 'jak', 'zdrowie']

def find_short_words(list):
    short_words = []
    for word in list:
        if len(word) < 5:
            short_words.append(word)

    return short_words

print(find_short_words(a))
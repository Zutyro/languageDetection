

def main():
    en_chars = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']


    en_corpus_string = corpus_to_string("en_corpus.txt", en_chars)
    print(en_corpus_string)

    en_unigrams, en_bigrams, en_trigrams = get_ngrams(en_corpus_string)
    print(en_unigrams)
    print(en_bigrams)
    print(en_trigrams)




def corpus_to_string(corpus, chars):
    file = open(corpus, 'r')
    lines = file.readlines()
    corpus_string = ""

    for line in lines:
        for char in line:
            if char.lower() in chars:
                corpus_string = corpus_string + char.lower()
                print(char)
                continue
            corpus_string = corpus_string + ' '

    return corpus_string




def get_ngrams(corpus_string):
    unigrams = {}
    bigrams = {}
    trigrams = {}

    for x,char in enumerate(corpus_string):
        if x < len(corpus_string)-2:
            next_char1 = corpus_string[x+1]
            next_char2 = corpus_string[x+2]
            trigrams[char+next_char1+next_char2] = trigrams.get(char+next_char1+next_char2, 0) + 1
        if x < len(corpus_string)-1:
            next_char = corpus_string[x+1]
            bigrams[char+next_char] = bigrams.get(char+next_char, 0) + 1
        unigrams[char] = unigrams.get(char, 0) + 1

    return unigrams, bigrams, trigrams


if __name__ == '__main__':
    main()
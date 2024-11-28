import matplotlib.pyplot as plt


def main():
    en_chars = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']


    en_corpus_string = corpus_to_string("en_corpus.txt", en_chars)
    print(en_corpus_string)

    en_unigrams, en_bigrams, en_trigrams = get_ngrams(en_corpus_string)
    print(en_unigrams)
    print(en_bigrams)
    print(en_trigrams)

    en_unigram_freq, en_bigram_freq, en_trigram_freq = get_frequencies(en_unigrams, en_bigrams, en_trigrams,en_corpus_string)
    print(en_unigram_freq)
    print(en_bigram_freq)
    print(en_trigram_freq)

    plot_frequencies(en_unigram_freq, en_bigram_freq, en_trigram_freq, 20)







def plot_frequencies(unigram_freq, bigram_freq, trigram_freq, size):
    ngrams = (unigram_freq, bigram_freq, trigram_freq)
    for ngram in ngrams:
        nigram_freq_sorted = dict(sorted(ngram.items(), key=lambda x: x[1], reverse=True))
        plt.bar(list(nigram_freq_sorted.keys())[0:size], list(nigram_freq_sorted.values())[0:size], color='blue')
        plt.show()



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

def get_frequencies(unigrams, bigrams, trigrams, corpus_string):
    unigram_freq = {}
    bigram_freq = {}
    trigram_freq = {}
    corpus_len = len(corpus_string)

    for x in unigrams:
        unigram_freq[x] = unigrams.get(x) / corpus_len
    for x in bigrams:
        bigram_freq[x] = bigrams.get(x) / (corpus_len/2)
    for x in trigrams:
        trigram_freq[x] = trigrams.get(x) / (corpus_len/3)

    return unigram_freq, bigram_freq, trigram_freq



if __name__ == '__main__':
    main()
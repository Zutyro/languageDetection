from matplotlib import pyplot as plt



def plot_frequencies(unigram_freq, bigram_freq, trigram_freq, size):
    ngrams = (unigram_freq, bigram_freq, trigram_freq)
    for ngram in ngrams:
        ngram_freq_sorted = dict(sorted(ngram.items(), key=lambda x: x[1], reverse=True))
        plt.bar(list(ngram_freq_sorted.keys())[0:size], list(ngram_freq_sorted.values())[0:size], color='blue')
        plt.show()



def corpus_to_string(corpus, chars):
    file = open(corpus, 'r', encoding='utf8')
    lines = file.readlines()
    corpus_string = ""
    corpus_string_count = 0

    for line in lines:
        for char in line:
            if char.lower() in chars:
                corpus_string = corpus_string + char.lower()
                corpus_string_count += 1
                continue
            if len(corpus_string) > 1 and corpus_string[corpus_string_count-1] != ' ':
                corpus_string = corpus_string + ' '
                corpus_string_count += 1

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

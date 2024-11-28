import ngrams as ng


def main():
    en_chars = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']


    en_corpus_string = ng.corpus_to_string("en_corpus.txt", en_chars)
    en_unigrams, en_bigrams, en_trigrams = ng.get_ngrams(en_corpus_string)
    en_unigram_freq, en_bigram_freq, en_trigram_freq = ng.get_frequencies(en_unigrams, en_bigrams, en_trigrams, en_corpus_string)

    ng.plot_frequencies(en_unigram_freq, en_bigram_freq, en_trigram_freq, 20)










if __name__ == '__main__':
    main()
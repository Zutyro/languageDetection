from venv import logger

import ngrams as ng


def main():
    en_chars = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cs_chars = ['a', 'á', 'b', 'c', 'č', 'd', 'ď', 'e', 'é', 'ě', 'f', 'g', 'h', 'i', 'í', 'j', 'k', 'l', 'm', 'n',
                'ň', 'o', 'ó', 'p', 'q', 'r', 'ř', 's', 'š', 't', 'ť', 'u', 'ú', 'ů', 'v', 'w', 'x', 'y', 'ý', 'z', 'ž',]
    sk_chars = ['a', 'á', 'ä', 'b', 'c', 'č', 'd', 'ď', 'dz', 'dž', 'e', 'é', 'f', 'g', 'h', 'ch', 'i', 'í', 'j', 'k',
                'l', 'ĺ', 'ľ', 'm', 'n',
                'ň', 'o', 'ó', 'ô', 'p', 'q', 'r', 'ŕ', 's', 'š', 't', 'ť', 'u', 'ú', 'v', 'w', 'x', 'y', 'ý', 'z', 'ž',]
    pl_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z'
                , 'ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż']
    gr_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'ä', 'ö', 'ü', 'ß']



    print("Converting corpus to string")
    en_corpus_string = ng.corpus_to_string("cs3.txt", cs_chars)
    print(en_corpus_string)
    print("Counting ngrams")
    en_unigrams, en_bigrams, en_trigrams = ng.get_ngrams(en_corpus_string)
    print("Calcucalting frequencies")
    en_unigram_freq, en_bigram_freq, en_trigram_freq = ng.get_frequencies(en_unigrams, en_bigrams, en_trigrams, en_corpus_string)
    print("Plotting graphs")
    ng.plot_frequencies(en_unigram_freq, en_bigram_freq, en_trigram_freq, 20)










if __name__ == '__main__':
    main()
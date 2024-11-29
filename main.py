from math import log
from random import random, randint
from venv import logger

from numpy.random import random_integers

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
    de_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'ä', 'ö', 'ü', 'ß']


    #Volá funkce pro získání frekvencí všech jazyků
    en_freqs = list(get_all_needed('en3.txt', en_chars))
    cs_freqs = list(get_all_needed('cs3.txt', cs_chars))
    sk_freqs = list(get_all_needed('sk3.txt', sk_chars))
    pl_freqs = list(get_all_needed('pl3.txt', pl_chars))
    de_freqs = list(get_all_needed('de3.txt', de_chars))

    #Příklad české věty
    text_ngrams = choose_ngrams('Tohle je dlouhá věta určená hlavně pro to aby byla pravděpodobnost větší')
    en_chance = get_chance(text_ngrams,en_freqs)
    cs_chance = get_chance(text_ngrams,cs_freqs)
    sk_chance = get_chance(text_ngrams,sk_freqs)
    pl_chance = get_chance(text_ngrams,pl_freqs)
    de_chance = get_chance(text_ngrams,de_freqs)
    chance_dict = {"gr": de_chance, "en": en_chance, "sk": sk_chance, "pl": pl_chance, "cs": cs_chance}
    highest_chance = max(chance_dict, key=chance_dict.get)
    print('Výsledek první věty - ' + highest_chance)

    #Příklad anglické věty
    text_ngrams = choose_ngrams('This is a long sentence designed mainly to make the probability higher')
    en_chance = get_chance(text_ngrams, en_freqs)
    cs_chance = get_chance(text_ngrams, cs_freqs)
    sk_chance = get_chance(text_ngrams, sk_freqs)
    pl_chance = get_chance(text_ngrams, pl_freqs)
    de_chance = get_chance(text_ngrams, de_freqs)
    chance_dict = {"gr": de_chance, "en": en_chance, "sk": sk_chance, "pl": pl_chance, "cs": cs_chance}
    highest_chance = max(chance_dict, key=chance_dict.get)
    print('Výsledek druhé věty - ' + highest_chance)

    #Příklad slovenské věty
    text_ngrams = choose_ngrams('Toto je dlhá veta určená hlavne na to aby bola pravdepodobnosť väčšia')
    en_chance = get_chance(text_ngrams, en_freqs)
    cs_chance = get_chance(text_ngrams, cs_freqs)
    sk_chance = get_chance(text_ngrams, sk_freqs)
    pl_chance = get_chance(text_ngrams, pl_freqs)
    de_chance = get_chance(text_ngrams, de_freqs)
    chance_dict = {"gr": de_chance, "en": en_chance, "sk": sk_chance, "pl": pl_chance, "cs": cs_chance}
    highest_chance = max(chance_dict, key=chance_dict.get)
    print('Výsledek třetí věty - ' + highest_chance)

    #Příklad polské věty
    text_ngrams = choose_ngrams('To długie zdanie które ma głównie na celu zwiększenie prawdopodobieństwa')
    en_chance = get_chance(text_ngrams, en_freqs)
    cs_chance = get_chance(text_ngrams, cs_freqs)
    sk_chance = get_chance(text_ngrams, sk_freqs)
    pl_chance = get_chance(text_ngrams, pl_freqs)
    de_chance = get_chance(text_ngrams, de_freqs)
    chance_dict = {"gr": de_chance, "en": en_chance, "sk": sk_chance, "pl": pl_chance, "cs": cs_chance}
    highest_chance = max(chance_dict, key=chance_dict.get)
    print('Výsledek čtvrté věty - ' + highest_chance)

    #Příklad německé věty
    text_ngrams = choose_ngrams('Dies ist ein langer Satz der hauptsächlich dazu gedacht ist die Wahrscheinlichkeit zu erhöhen')
    en_chance = get_chance(text_ngrams, en_freqs)
    cs_chance = get_chance(text_ngrams, cs_freqs)
    sk_chance = get_chance(text_ngrams, sk_freqs)
    pl_chance = get_chance(text_ngrams, pl_freqs)
    de_chance = get_chance(text_ngrams, de_freqs)
    chance_dict = {"gr": de_chance,"en": en_chance,"sk": sk_chance,"pl": pl_chance, "cs": cs_chance}
    highest_chance = max(chance_dict, key=chance_dict.get)
    print('Výsledek páté věty - ' + highest_chance)



#Vrací šanci, že je text psaný v daném jazyce podle frekencí ngramů
def get_chance(text_ngrams, freqs):
    chance = 0
    for x in text_ngrams:
        x = x.lower()
        match len(x):
            case 1:
                chance = chance + log(freqs[0].get(x, min(freqs[0].values()) / 2))
                continue
            case 2:
                chance = chance + log(freqs[1].get(x, min(freqs[1].values()) / 2))
                continue
            case 3:
                chance = chance + log(freqs[2].get(x, min(freqs[2].values()) / 2))
    return chance


#Volá všechny funkce potřebné pro získání frekvencí ngramů s možností vytvoření jejich grafů.
def get_all_needed(corpus, chars):
    corpus_string = ng.corpus_to_string(corpus, chars)
    unigrams, bigrams, trigrams = ng.get_ngrams(corpus_string)
    unigram_freq, bigram_freq, trigram_freq = ng.get_frequencies(unigrams, bigrams, trigrams,
                                                                 corpus_string)
    # print("Plotting graphs")
    # ng.plot_frequencies(unigram_freq, bigram_freq, trigram_freq, 20)

    return unigram_freq, bigram_freq, trigram_freq



#Vybírá ngramy ze zadaného textu, náhodně rozhodne jestli unigram, bigram nebo trigram. Posouvá se ve větě o délku vybraného ngramu.
def choose_ngrams(text):
    ngrams = list()
    text_count = 0

    if len(text) <= 10:
        ngrams = list(text)
        return ngrams
    while len(ngrams) < 10 and text_count < len(text):
        choice = randint(1,3)
        match choice:
            case 1:
                ngrams.append(text[text_count])
                text_count = text_count +1
                continue
            case 2:
                if len(text) - text_count >= 2:
                    ngrams.append(text[text_count]+text[text_count+1])
                    text_count = text_count + 2
                continue
            case 3:
                if len(text) - text_count >= 3:
                    ngrams.append(text[text_count] + text[text_count + 1] + text[text_count+2])
                    text_count = text_count + 3
                continue

    return ngrams


if __name__ == '__main__':
    main()
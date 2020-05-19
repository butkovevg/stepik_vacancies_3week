import pymorphy2


def matching_words_numerals(word, numeral):
    morph = pymorphy2.MorphAnalyzer().parse(word)[0]
    return morph.make_agree_with_number(numeral).word

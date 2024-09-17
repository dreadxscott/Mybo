from pykakasi import kakasi
import jaconv as jcv

kks = kakasi()


def transliterate_romaji_to_hiragana(text):
    liter = jcv.alphabet2kana(text)
    print(liter)

def transliterate_kana_to_romaji(text):
    item = kks.convert(text)
    print(item[0]['hira'], item[0]['kana'])


text = input("Transliterate: ")
transliterate_romaji_to_hiragana(text)

text2 = input("Transliterate: ")
transliterate_kana_to_romaji(text2)
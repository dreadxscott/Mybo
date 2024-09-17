#services/transliteration

class TransliterationService():
    from pykakasi import kakasi
    import jaconv as jcv

    kks = kakasi()

    def transliterate_romaji_to_hiragana(self,text):
        liter = self.jcv.alphabet2kana(text)
        return liter

    def transliterate_kana_to_romaji(self,text):
        item = self.kks.convert(text)
        return { 'Hiragana' : item[0]['hira'], 
                 'Katakana' : item[0]['kana']}


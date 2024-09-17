#aozora_parser_service.py
import urllib.request
from bs4 import BeautifulSoup
import lxml
import re

class AozoraParser():

    def open_html(self, url):
        with urllib.request.urlopen(url) as response:
            byte_data = response.read()
            html_content = byte_data.decode(encoding='shift_jis', errors='ignore')

            soup = BeautifulSoup(html_content, 'html.parser')
            return soup
        
    def find_all_ruby(self, soup):
        ruby = soup.find_all('ruby')
        return ruby
    
    def parse(self, ruby):

        parsed = {}
        for r in ruby:
            kanji = r.text
            furigana = r.rt.text
            parsed[kanji] = furigana
        
        return parsed
    
    def write_map(self, parsed_data):
        parsed_data = str(parsed_data)
        try:
            with open("parsed_data.txt", "w", encoding='utf-8', errors='ignore') as f:
                f.write(parsed_data)
        except Exception as e:
            print(e)
    
    
    def recode_utf(self, soup):
        soup = str(soup)
        with open("recoded_data.txt", "w", encoding='utf-8', errors='ignore') as f:
            f.write(soup)
    def main(self, filepath):
        #make the soup
        main_soup = self.open_html(filepath)

        #get the ruby
        main_ruby = self.find_all_ruby(main_soup)

        #parse the data
        main_parsed = self.parse(main_ruby)

        #wrie out the ruby
        main_map = self.write_map(main_parsed)

        #recode
        main_recode = self.recode_utf(main_soup)


        

#here's our story
baseurl = "https://www.aozora.gr.jp/cards/000879/files/174_15163.html"

if __name__ == "__main__":
    AP = AozoraParser()
    AP.main(baseurl)




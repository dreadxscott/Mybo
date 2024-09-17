from django.core.management.base import BaseCommand, CommandParser, CommandError
from japanese_learner.models import Word, Sentence
from django.db.models import Q
from django.apps import apps

import pandas as pd
import re

def clean_text(text):
    # Strip leading and trailing spaces
    text = text.strip()
    
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    
    # Optional: Convert to lowercase
    text = text.lower()
    
    return text

class Command(BaseCommand):
    help = "Retrieves data from files, uploads it to models"

    #what arguments do we take
    def add_arguments(self, parser):
        parser.add_argument('filename', help='Path to the csv file')
        parser.add_argument('type',choices=['Word','Sentence'],help="Sentence or Word")
    
    #handling the arguments to get the data from a file and load it to the DB
    def handle(self, *args, **options):
        #importing models dynamically
        WordBank = apps.get_model('japanese_learner','Word')
        SentenceBank = apps.get_model('japanese_learner', 'Sentence')

        csv_file = options['filename']
        type = options['type']

        #check if it's a valid type being given in the argument
        if type not in ['Word','Sentence']:
            raise ValueError(f"Invalid type: {type}. Must be either Word or Sentence")
    
        
        #now to upload the data
        try:
            if type == "Word":
                #Read Data
                df = pd.read_csv(csv_file)
                df = df.fillna('')
                df = df.map(clean_text)
                self.stdout.write(self.style.SUCCESS("Datafrane successfully created"))

            elif type == "Sentence":
                #technically not a CSV but
                df = pd.read_csv(csv_file, delimiter='|')
                df = df.fillna('')
                df = df.map(clean_text)
                self.stdout.write(self.style.SUCCESS("Datafrane successfully created"))

        except Exception as e:
            print(f"An error occurred: {e}")

        #get the word data
        if df is not None and type=='Word':
            for index, row in df.iterrows():
                word_inst = Word.objects.create(
                    hiragana = row['hiragana'],
                    katakana = row['katakana'],
                    kanji = row['kanji'],
                    meaning = row['meaning'],
                    points = 3
                )
        
        #get the sentence data
        elif df is not None and type == 'Sentence':
            for index, row in df.iterrows():
                words = Word.objects.filter(Q(hiragana=row['keyword']) 
                                            | Q(katakana=row['keyword'])
                                            | Q(kanji=row['keyword']))
                word = words.first()
                sent_inst = Sentence.objects.create(
                    sentence = row['sentence'],
                    meaning = row['meaning'],
                    keyword = word,
                    points = 5
                )
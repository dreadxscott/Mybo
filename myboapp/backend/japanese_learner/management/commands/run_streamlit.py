#make_flashcards.py
from django.core.management.base import BaseCommand
import subprocess

class Command(BaseCommand):
    help = 'Run the Streamlit app for translation and transliteration'

    def handle(self, *args, **kwargs):
        self.stdout.write("Running the streamlit app")
        subprocess.run("streamlit","run",r"C:\Users\colli\Python\Mybo\transliterate.py")
        

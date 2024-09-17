#make_questions 
from django.core.management.base import BaseCommand, CommandError
from japanese_learner.models import Word, Sentence, MultipleChoiceQuestion, InputQuestion
from django.apps import apps

class Command(BaseCommand):
    help = "Make the questions based on data in the join"

    def handle(self, *args, **options):
        #Dyanmically importing models
        MCQuestion = apps.get_model('japanese_learner', 'MultipleChoiceQuestion')
        QAQuestion = apps.get_model('japanese_learner', 'InputQuestion')
        Word = apps.get_model('japanese_learner', 'Word')
        Sentence = apps.get_model('japanese_learner', 'Sentence')

        #creating multiple choice questions based on word
        for obj in Word.objects.all():
            word_text = obj.kanji or obj.hiragana or obj.katakana or "No valid word available"
            MCQuestion.objects.get_or_create(
                question_text = "What does {word} mean?".format(word=word_text),
                correct_answer = obj,
            )
            self.stdout.write(self.style.SUCCESS("Question successfully created"))

        #creating qa questions based on sentence
        for obj in Sentence.objects.all():
            QAQuestion.objects.get_or_create(
                sentence = obj,
                word = obj.keyword,
                answer = obj.meaning,
                question = f"What does {obj.sentence} mean?",
                story = obj.story
            )


#/services/answer_comp_service.py
from japanese_learner.models import InputQuestion
from django.apps import apps

class ComparisonService():
    def compare_answers(self, string1, string2):
        return (string1.strip().lower() == string2.strip().lower())
    
    def check_answer(self, text_dict):
        import string
        #import models dynamically
        InputQuestion = apps.get_model('japanese_learner','InputQuestion')

        question = text_dict['question']
        answer = text_dict['answer']

        #use the text to get the question, get the answer and compare it
        question_obj = InputQuestion.objects.filter(question=question)
        
        return( "Correct! よくできました" if self.compare_answers(question_obj.get().answer, answer) else "Incorrect. まてみよう")
        
        

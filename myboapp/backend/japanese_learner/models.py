from django.db import models
import random

class Story(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

# Create your models here.
class Word(models.Model):
    hiragana = models.CharField(max_length=200, null=True, blank=True)
    katakana = models.CharField(max_length=200, blank=True, null=True)
    kanji = models.CharField(max_length=200, blank=True, null=True)
    meaning = models.TextField()
    points = models.IntegerField()
    story = models.ForeignKey(Story, null=True, related_name="words",
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.kanji or self.hiragana or self.katakana

class Sentence(models.Model):
    sentence = models.TextField()
    meaning = models.TextField()
    keyword = models.ForeignKey(Word, on_delete=models.PROTECT)
    points = models.IntegerField(default=5)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="sentences", 
                              null=True) #allowing null for existing data

    def __str__(self):
        return f"Sentence: {self.sentence}; keyword: {self.keyword}"

class MultipleChoiceQuestion(models.Model):
    #choices for your question
    #will likely edit later

    question_text = models.CharField(max_length=200)
    correct_answer = models.ForeignKey(Word, related_name="correct_answer", on_delete=models.CASCADE, null=True)

    def get_points(self):
        return self.word.points
    
    def get_story(self):
        # Access the story through the word
        return self.correct_answer.story
    def __str__(self):
        return self.question_text
    
class InputQuestion(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE)

    def get_points(self):
        return self.word.points or self.sentence.points
    
    def __str__(self):
        return self.question
    
    def get_story(self):
        return self.sentence.story
from django.db import models

#a dictionary to store kanji, hiragana, onyomi,kuniyomi, meaning, usages, frequecy
class KanjiDictionary(models.Model):

    character = models.CharField(max_length=10)
    onyomi = models.JSONField(default=list)  # Store onyomi readings as a list
    kunyomi = models.JSONField(default=list)  # Store kunyomi readings as a list
    meaning = models.TextField()
    usage_examples = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.kanji


from rest_framework import serializers
from japanese_learner.models import Story, Word, Sentence, MultipleChoiceQuestion, InputQuestion

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'title']  # Include any other fields from the Story model as needed

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['hiragana', 'katakana', 'kanji', 'meaning']

class SentenceSerializer(serializers.ModelSerializer):
    keyword = serializers.StringRelatedField()  # Display the string representation of the keyword

    class Meta:
        model = Sentence
        fields = "__all__"

class MultipleChoiceQuestionSerializer(serializers.ModelSerializer):
    points = serializers.IntegerField(source='correct_answer.points')
    story = StorySerializer(source='correct_answer.story')
    correct_answer = WordSerializer()

    class Meta:
        model = MultipleChoiceQuestion
        fields = ['question_text', 'correct_answer', 'points', 'story']

    def get_points(self, obj):
        return obj.get_points()

    def get_story(self, obj):
        return obj.get_story()

class InputQuestionSerializer(serializers.ModelSerializer):
    points = serializers.IntegerField(source='sentence.points')
    story = StorySerializer(source='sentence.story')
    answer = serializers.CharField(source='sentence.meaning')
    sentence = SentenceSerializer()
    word = WordSerializer(source="sentence.keyword")

    class Meta:
        model = InputQuestion
        fields = "__all__"
    def get_points(self, obj):
        return obj.get_points()

    def get_story(self, obj):
        return obj.get_story()
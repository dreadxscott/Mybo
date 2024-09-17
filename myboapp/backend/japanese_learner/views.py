from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from .serializers import SentenceSerializer, MultipleChoiceQuestionSerializer, InputQuestionSerializer, WordSerializer
from .models import Sentence, Story, Word, MultipleChoiceQuestion, InputQuestion
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from japanese_learner.services import transliteration_service as TS
from japanese_learner.services import comparison_service as CS
import json
from rest_framework.permissions import IsAuthenticated

@csrf_exempt  # This disables CSRF protection for this endpoint, make sure to handle it securely in production
def handle_form_submission(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            question = data.get('question')  # Extract the input data
            input_data = data.get('answer')
    
            # Handle your data here (save to DB, process, etc.)
            if input_data:
                # Compare the response to the answer
                comp_serv = CS.ComparisonService()
                res = comp_serv.check_answer({'question': question, 'answer': input_data})
                return JsonResponse({
                    'status': 'success',
                    'message': 'Form received!',
                    'input': res,  # Send the transliteration back as part of the response
                })
            else:
                return JsonResponse({
                    'status': 'error',
                    'message': 'No input provided',
                }, status=400)
        except json.JSONDecodeError:
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid JSON',
            }, status=400)


def index(request):
    return HttpResponse("Hi there! Welcome to Mybo, your Japanese Language Learning Assistant! ^ _ ^\n")

"""
Game (Japanese learner) - the game where you go through the story learning Japanese through Hanasuke the Chihuahua and Spider Thread
	Inside the game we'll need a view for the story and the flashcard game itself
	In the story, we'll need a view for cultural info when that becomes relevant
	User progress (learned words, mastered words, points, current level)
"""

def about_us(request):
    response = """
        About me:\n
        Hello! こんにちは! Welcome! ようこそ!\n
        My name is Collin Francis, the creator of Mybo! I had the idea for this project last year as\n
        having been studying Japanese since I was a young boy. My interest in the language started\n
        watching anime like Dragon Ball Z and Yu Yu Hakusho with my older brother and our friends.\n
        Continuing to learn about the culture and history, I gained a deep love and respect for the\n
        culture. Wanting to share this love with the world, I decided to make Mybo, an online\n
        game to help fellow Japanese learners practice their reading, vocabulary, and understanding in a\n
        fun and interactive way. Here, you'll find different stories to read that will test your skills.\n
        teach you vocabulary, and help you along the way.

        That's what the name meansa fter all. Mybo is a mix of the English word My and the Japanese word あいぼう\n
        (aibo), meaning partner.\n
        Have fun!
        よろしくおねがいします！
        """
    return HttpResponse(response)

def mybo(request):
    context = {
        'title': 'Mybo Landing Page',
    }
    return render(request,'japanese_learner/index.html',context)

class WordSerializerView(generics.ListAPIView):
    serializer_class = WordSerializer
    queryset = Word.objects.all()
    permission_classes =[IsAuthenticated]    

class StorySentencesView(generics.ListAPIView):
    serializer_class = SentenceSerializer
    permission_classes =[IsAuthenticated]

    def get_queryset(self):
        story_id = self.kwargs['story_id']
        print("Captured story_id:", story_id)  # Add this line for debugging
        return Sentence.objects.filter(story=story_id).order_by('id')


class MultipleChoiceQuestionView(generics.ListAPIView):
    queryset = MultipleChoiceQuestion.objects.all()
    serializer_class = MultipleChoiceQuestionSerializer

    permission_classes =[IsAuthenticated]

class InputQuestionView(generics.ListAPIView):
    queryset = InputQuestion.objects.all()
    serializer_class = InputQuestionSerializer
    permission_classes =[IsAuthenticated]
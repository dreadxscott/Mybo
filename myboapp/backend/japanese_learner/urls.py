#urls.py for japanese_learner
from django.urls import path
from .views import StorySentencesView, MultipleChoiceQuestionView, InputQuestionView, WordSerializerView

from . import views

urlpatterns = [
    path("", views.index, name='Index'),
    path("about/", views.about_us, name="About"),
    path("mybo/", views.mybo, name="Mybo"),
    path('api/story/<int:story_id>/sentences/', StorySentencesView.as_view(), name='story-sentences'),
    path('api/mcq/', MultipleChoiceQuestionView.as_view(), name='mcq-list'),
    path('api/qa/', InputQuestionView.as_view(), name='qa-list'),
    path('api/form-submit/', views.handle_form_submission, name='form-submit'),
    path('api/words/', WordSerializerView.as_view(), name='words')
]
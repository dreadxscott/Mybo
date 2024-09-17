from django.contrib import admin
from .models import *

admin.site.register(Word)
admin.site.register(Sentence)
admin.site.register(Story)
admin.site.register(MultipleChoiceQuestion)
admin.site.register(InputQuestion)

class SentenceAdmin(admin.ModelAdmin):
    list_display = ('sentence', 'keyword', 'points')  # Customize the columns shown in the list
    search_fields = ('sentence',)  # Add a search box for sentences
    list_filter = ('keyword',)  # Add a filter by keyword
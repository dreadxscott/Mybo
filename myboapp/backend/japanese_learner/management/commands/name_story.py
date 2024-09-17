from django.core.management.base import BaseCommand, CommandError
from japanese_learner.models import Sentence, Story, Word

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("title", help="Title of the story")
        parser.add_argument("--content", help="Story topic")
    
    def handle(self, *args, **options):
        title = options["title"]
        content = options.get("content", "")

        # Fetch or create the story instance
        story_inst, created = Story.objects.get_or_create(title=title, defaults={"description": content})

        if created:
            self.stdout.write(self.style.SUCCESS(f"Created new story: {title}"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Using existing story: {title}"))

        for sentence in Sentence.objects.all():
            if sentence.story is None:    
                sentence.story = story_inst
                sentence.save()
                self.stdout.write(self.style.SUCCESS(f"Updated sentence {sentence.id} with story: {title}"))

        for word in Word.objects.all():
            if not word.story:
                word.story = story_inst
                word.save()
                self.stdout.write(self.style.SUCCESS(f"Updated word {word.id} with story: {title}"))

# Generated by Django 5.1.1 on 2024-09-09 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('japanese_learner', '0002_story_sentence_points_alter_word_points_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='points',
            field=models.IntegerField(),
        ),
    ]

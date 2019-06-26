# Generated by Django 2.2.1 on 2019-05-25 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0011_answer_hindsight_question_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer_type',
            field=models.CharField(choices=[('Multiple Choice', 'Multiple Choice'), ('Comment', 'Comment')], default='Multiple Choice', max_length=50),
            preserve_default=False,
        ),
    ]
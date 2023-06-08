# Generated by Django 4.2.1 on 2023-06-04 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0003_alter_quiz_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='difficulty',
            field=models.CharField(choices=[('medium', 'medium'), ('hard', 'hard'), ('easy', 'easy')], max_length=120),
        ),
    ]

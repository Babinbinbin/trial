from django.db import models
import random
# Create your models here.
DIFF_CHOICES ={
    ("easy","easy"),
    ("medium","medium"),
    ("hard","hard")
}

class Quiz(models.Model):
    name = models.CharField(max_length= 120)
    topic = models.CharField(max_length= 120)
    number_of_questions = models.IntegerField()
    required_score_to_pass  = models.IntegerField(help_text="required score")
    time  = models.IntegerField(help_text="duration of quiz in minutes")
    difficulty = models.CharField(max_length=120,choices=DIFF_CHOICES)

    def __str__(self):
        return f"{self.name}-{self.topic}"
    
    def get_questions(self): 
        quest =list(self.question_set.all())
        random.shuffle(quest)
        return quest[:]
    
    class Meta:
        verbose_name_plural ='Quizes'




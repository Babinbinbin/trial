from django.db import models
import uuid
import random
# Create your models here.

class BaseModels(models.Model):
    uid = models.UUIDField(primary_key=True,default = uuid.uuid4)
    created_at = models.DateField(auto_now=True )
    updated_at=models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModels):
    category_name = models.CharField(max_length =100)

    def __str__(self) :
        return self.category_name

class Question(BaseModels):
    category = models.ForeignKey(Category,related_name = "category",on_delete = models.CASCADE)
    question = models.CharField(max_length=100)
    marks = models.IntegerField(default = 5)

    def __str__(self):
        return self.question
    
    def get_answer(self):
        return self.answer_set.all()

class Answer(BaseModels):
    question = models.ForeignKey(Question,related_name="question_answer",on_delete = models.CASCADE)
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default = False)

    def __str__(self) :

        return (self.text).capitalize()


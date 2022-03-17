from time import timezone
from django.db import models
from django.db import migrations

class Migration(migrations.Migration):
    atomic = False

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
    #saber se a data de publicacao e maior ou menor que um dia 
    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text

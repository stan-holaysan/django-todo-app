from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    llm_response = models.CharField(max_length=500)

    def __str__(self):
        return self.title
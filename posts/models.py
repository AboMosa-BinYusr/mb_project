from django.db import models

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()

    def __str__(self):
        return self.text
    
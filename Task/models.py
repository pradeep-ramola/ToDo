from django.db import models

# Create your models here.
class Add(models.Model):
    mytask = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.mytask

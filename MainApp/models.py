from django.db import models


# Create your models here.
class DataScript(models.Model):
    script = models.TextField(max_length=2000)
    image = models.ImageField(null=True, blank=True)
    count = models.IntegerField(default=0)


class ScriptInput(models.Model):
    user_that_input = models.ForeignKey(DataScript, on_delete=models.SET_NULL, null=True)
    inputText = models.TextField(max_length=2000, null=True)

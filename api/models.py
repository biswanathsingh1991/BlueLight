from django.db import models


# Create your models here.


class TestModel(models.Model):

    test_name = models.CharField(max_length=250)
    test_about = models.CharField(max_length=1000)
    test_id = models.IntegerField()

    def __str__(self):
        return self.test_name

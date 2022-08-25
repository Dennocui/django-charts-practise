from django.db import models

# Create your models here.


class Data(models.Model):
    qty = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return "{}".format(self.date)

    class Meta:
        verbose_name = "Data"
        verbose_name_plural = "Data"
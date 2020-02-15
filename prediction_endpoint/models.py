from django.db import models

class Prediction(models.Model):
    gsv_id = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    label = models.IntegerField()
    confidence = models.FloatField()
    update_time = models.DateTimeField()

    def __str__(self):
        return "({},{}): {}".format(self.latitude,
                                    self.longitude,
                                    self.label)
# Create your models here.

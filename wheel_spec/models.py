from django.db import models

class WheelSpecification(models.Model):
    formNumber = models.CharField(max_length=50, unique=True)
    submittedBy = models.CharField(max_length=50)
    submittedDate = models.DateField()
    fields = models.JSONField()  # store the nested fields dict

    def __str__(self):
        return self.formNumber
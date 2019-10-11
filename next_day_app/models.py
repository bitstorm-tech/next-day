from django.db import models


class PlanningItem(models.Model):
    name = models.TextField()
    description = models.TextField()

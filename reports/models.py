from django.db import models

# Create your models here.
from django.db import models

COUNTRIES = (
        ('uk', 'UK'),
        ('us', 'USA'),
        ('in', 'India'),
    )
LABELS = (
    ('0', 'NEGATIVE'),
    ('1', 'POSITIVE'),
    ('2', 'NEUTRAL'),
)


class Report(models.Model):
    goodness = models.CharField(max_length=2)
    country = models.CharField(max_length=2, choices=COUNTRIES)
    pub_date = models.DateTimeField('date published', blank=True)

    def __str__(self):
        return self.goodness

from typing import Tuple

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


class Article(models.Model):
    title = models.CharField(max_length=1000)
    content = models.CharField(max_length=10000)
    country = models.CharField(max_length=2, choices=COUNTRIES)
    pub_date = models.DateTimeField('date published', blank=True)
    analysed_at = models.DateTimeField('date article created', blank=True)

    label = models.CharField(max_length=1, choices=LABELS)

    def __str__(self):
        return self.content


class Choice(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    chosen_label = models.CharField(max_length=1, choices=LABELS)
    votes = models.IntegerField(default=0)
    created = models.DateTimeField('date article created')
    updated = models.DateTimeField('date article updated')


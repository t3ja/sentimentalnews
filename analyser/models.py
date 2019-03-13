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


class ArticleManager(models.Manager):
    def by_label(self, label):
        return super().get_queryset().filter(label=label)

    def latest(self):
        return super().get_queryset().limit(50).order_by('-created_at')


class Article(models.Model):
    title = models.CharField(max_length=2000, blank=True, null=True)
    description = models.CharField(max_length=5000, blank=True, null=True)
    author = models.CharField(max_length=2000, blank=True, null=True)
    content = models.CharField(max_length=10000, blank=True, null=True)
    country = models.CharField(max_length=2, choices=COUNTRIES)
    published_at = models.DateTimeField('date published', blank=True, auto_now_add=True)
    analysed_at = models.DateTimeField('date article classified', null=True, blank=True)
    source = models.CharField(max_length=2000, blank=True, null=True)
    url = models.CharField(max_length=2000, blank=True, null=True)
    label = models.CharField(max_length=1, choices=LABELS, blank=True, null=True)

    def __str__(self):
        return self.title

    objects = models.Manager()
    ArticleManager = ArticleManager()

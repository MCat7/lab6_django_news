from django.db import models

# Create your models here.
class NewsHeadline(models.Model):
    news_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')


class TextNews(models.Model):
    news = models.ForeignKey(NewsHeadline, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)


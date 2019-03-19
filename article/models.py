from django.db import models

# Create your models here.
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_heading = models.CharField(max_length=250)	
    article_xaxis_name = models.CharField(max_length=250)
    article_xaxis_data1 = models.IntegerField(max_length=250)
    article_xaxis_data2 = models.IntegerField(max_length=250)
    article_xaxis_data3 = models.IntegerField(max_length=250)
    article_xaxis_data4 = models.IntegerField(max_length=250)
    article_xaxis_data5 = models.IntegerField(max_length=250)
    article_xaxis_data6 = models.IntegerField(max_length=250)
    article_xaxis_data7 = models.IntegerField(max_length=250)
    article_xaxis_data8 = models.IntegerField(max_length=250)
    article_xaxis_data9 = models.IntegerField(max_length=250)
    article_xaxis_data10 = models.IntegerField(max_length=250)
    article_yaxis_name = models.TextField(max_length=250)
    article_yaxis_data1 = models.IntegerField(max_length=250)
    article_yaxis_data2 = models.IntegerField(max_length=250)
    article_yaxis_data3 = models.IntegerField(max_length=250)
    article_yaxis_data4 = models.IntegerField(max_length=250)
    article_yaxis_data5 = models.IntegerField(max_length=250)
    article_yaxis_data6 = models.IntegerField(max_length=250)
    article_yaxis_data7 = models.IntegerField(max_length=250)
    article_yaxis_data8 = models.IntegerField(max_length=250)
    article_yaxis_data9 = models.IntegerField(max_length=250)
    article_yaxis_data10 = models.IntegerField(max_length=250)


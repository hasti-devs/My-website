from django.db import models
class Article(models.Model):
    title = models.CharField(max_length=200,verbose_name="عنوان مقاله")
    content = models.TextField(verbose_name="متحوای مقاله")
    published_at = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ انتشار")

def __str__(self):
    return self.title

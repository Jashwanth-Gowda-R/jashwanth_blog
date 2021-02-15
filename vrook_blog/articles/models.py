from django.db import models

# Create your models here.

# run below commands after writing model code
# python manage.py makemigrations
# python manage.py migrate

class Articles(models.Model):
    title=models.CharField(max_length=250)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    thumbnail=models.ImageField(default='default.png',blank=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]+ ' .....'


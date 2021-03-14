from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.

# run below commands after writing model code
# python manage.py makemigrations
# python manage.py migrate

class Articles(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    # body=models.TextField()
    body = RichTextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING, )

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '..(continued!)'

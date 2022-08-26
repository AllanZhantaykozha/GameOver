from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField


class Game(models.Model):
    title = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField()
    release = models.DateField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    create_by = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')
    cpu = models.CharField(max_length=50)
    gpu = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    ram = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    steam = models.URLField(max_length=300)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detailgame', kwargs={'slug': self.slug}) 

    class Meta:
        ordering = ['-release']

class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
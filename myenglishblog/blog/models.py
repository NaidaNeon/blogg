from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name='topic')
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    video = models.FileField(upload_to="videos/%Y/%m/%d/", null=True) #, validators=[FileExtesionValidator(allowed_extensions=['MOV', 'mp4', 'avi', 'mkv', 'webm'])])
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Posted')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Last updated')
    is_published = models.BooleanField(default=True, verbose_name='Published')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
    
    class Meta:
        verbose_name = 'A Useful Blog'
        verbose_name_plural = 'A Useful Blog'
        ordering = ['-time_create', 'title']

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Category')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'
        ordering = ['id']
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

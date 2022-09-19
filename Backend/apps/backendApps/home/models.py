from django.db import models
from ckeditor.fields import RichTextField

class HomeTitleModel(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'HOME - Page Title'
        verbose_name_plural = 'HOME - Page Title'
        db_table = 'apps_backend_home_page_title'

    def __str__(self):
        return self.title

class HomeContentModel(models.Model):
    short_name = models.CharField(max_length=100)
    content = RichTextField()

    class Meta:
        verbose_name = 'HOME - Content'
        verbose_name_plural = 'HOME - Content'
        db_table = 'apps_backend_home_page_content'
        
    def __str__(self):
        return f"{self.id} - {self.short_name}"

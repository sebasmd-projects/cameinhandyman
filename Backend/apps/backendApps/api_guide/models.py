from django.db import models
from ckeditor.fields import RichTextField

class ApiGuideTitleModel(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'APIGuide - Page Title'
        verbose_name_plural = 'APIGuide - Page Title'
        db_table = 'apps_backend_api_guide_page_title'

    def __str__(self):
        return self.title

class ApiGuideContentModel(models.Model):
    short_name = models.CharField(max_length=100)
    content = RichTextField()

    class Meta:
        verbose_name = 'APIGuide - Content'
        verbose_name_plural = 'APIGuide - Content'
        db_table = 'apps_backend_api_guide_page_content'
        
    def __str__(self):
        return f"{self.id} - {self.short_name}"

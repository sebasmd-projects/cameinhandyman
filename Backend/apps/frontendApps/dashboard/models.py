from django.db import models
from ckeditor.fields import RichTextField


class DashBoardMetaModel(models.Model):
    key = models.CharField(
        "Llave",
        max_length=255,
        unique=True
    )
    
    page_title = models.CharField(
        "Titulo de la pagina",
        max_length=100
    )

    title = models.CharField(
        "Título",
        max_length=255
    )

    content = models.CharField(
        "Contenido",
        max_length=255,
        blank=True,
        null=True
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Meta Tags"
        verbose_name_plural = "Meta Tags"
        db_table = "apps_dashboard_metatags"
        ordering = ['key', 'id', 'title']

    def __str__(self):
        return f"{self.title} - {self.content}"


class BannerSectionModel(models.Model):
    description = RichTextField(
        "Descripción",
    )

    image = models.ImageField(
        "Imagen",
        upload_to='home/banner'
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = 'Banner Section'
        verbose_name_plural = 'Banner Section'
        db_table = "apps_dashboard_bannersection"
        ordering = ['id']

    def __str__(self):
        return self.id

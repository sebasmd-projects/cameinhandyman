# Generated by Django 4.0.6 on 2022-09-20 00:14

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerSectionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Descripción')),
                ('image', models.ImageField(upload_to='home/banner', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Banner Section',
                'verbose_name_plural': 'Banner Section',
                'db_table': 'apps_dashboard_bannersection',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DashBoardMetaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255, unique=True, verbose_name='Llave')),
                ('page_title', models.CharField(max_length=100, verbose_name='Titulo de la pagina')),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
                ('content', models.CharField(blank=True, max_length=255, null=True, verbose_name='Contenido')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Meta Tags',
                'verbose_name_plural': 'Meta Tags',
                'db_table': 'apps_dashboard_metatags',
                'ordering': ['key', 'id', 'title'],
            },
        ),
    ]

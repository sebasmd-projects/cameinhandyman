# Generated by Django 4.0.6 on 2022-09-16 05:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TVHandleCordsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='TV title (handleCords). Max 25 characters. Blank and Null are allowed.', max_length=25, null=True)),
                ('description', models.CharField(blank=True, help_text='TV description (handleCords). Max 50 characters. Blank and Null are allowed.', max_length=50, null=True)),
                ('price', models.CharField(help_text='TV price (handleCords). Max 10 characters.', max_length=10)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, help_text='Created', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Updated', verbose_name='Updated')),
                ('order', models.PositiveIntegerField(blank=True, default=0, help_text='Orden de visualización', null=True, verbose_name='Orden')),
            ],
            options={
                'verbose_name': 'TV Handle Cords',
                'verbose_name_plural': 'TV Handle Cords',
                'db_table': 'apps_tv_handle_cords',
                'ordering': ['order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='TVOtherInstallsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='TV title (otherInstalls). Max 25 characters. Blank and Null are allowed.', max_length=25, null=True)),
                ('description', models.CharField(blank=True, help_text='TV description (otherInstalls). Max 50 characters. Blank and Null are allowed.', max_length=50, null=True)),
                ('price', models.CharField(help_text='TV price (otherInstalls). Max 10 characters.', max_length=10)),
                ('img', models.ImageField(blank=True, null=True, upload_to='tv_other_installs/')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, help_text='Created', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Updated', verbose_name='Updated')),
                ('order', models.PositiveIntegerField(blank=True, default=0, help_text='Orden de visualización', null=True, verbose_name='Orden')),
            ],
            options={
                'verbose_name': 'TV Other Installs',
                'verbose_name_plural': 'TV Other Installs',
                'db_table': 'apps_tv_other_installs',
                'ordering': ['order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='TVQuestionsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='TV title (otherInstalls). Max 25 characters. Blank and Null are allowed.', max_length=25, null=True)),
                ('description', models.CharField(blank=True, help_text='TV description (otherInstalls). Max 50 characters. Blank and Null are allowed.', max_length=50, null=True)),
                ('price', models.CharField(blank=True, help_text='TV price (otherInstalls). Max 10 characters.', max_length=10, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='tv_questions/')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, help_text='Created', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Updated', verbose_name='Updated')),
                ('order', models.PositiveIntegerField(blank=True, default=0, help_text='Orden de visualización', null=True, verbose_name='Orden')),
            ],
            options={
                'verbose_name': 'TV Questions',
                'verbose_name_plural': 'TV Questions',
                'db_table': 'apps_tv_questions',
                'ordering': ['order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='TVSizeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='TV title (size). Max 25 characters. Blank and Null are allowed.', max_length=25, null=True)),
                ('description', models.CharField(blank=True, help_text='TV description (size). Max 50 characters. Blank and Null are allowed.', max_length=50, null=True)),
                ('size', models.CharField(help_text='TV size in inches (size). Max 10 characters', max_length=10)),
                ('price', models.CharField(help_text='TV price in usd (size). Max 10 characters', max_length=10)),
                ('img', models.ImageField(blank=True, null=True, upload_to='tv_size/')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, help_text='Created', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Updated', verbose_name='Updated')),
                ('order', models.PositiveIntegerField(blank=True, default=0, help_text='Orden de visualización', null=True, verbose_name='Orden')),
            ],
            options={
                'verbose_name': 'TV Size',
                'verbose_name_plural': 'TV Size',
                'db_table': 'apps_tv_size',
                'ordering': ['order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='TVSurfaceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='TV title (surface). Max 25 characters. Blank and Null are allowed.', max_length=25, null=True)),
                ('description', models.CharField(blank=True, help_text='TV description (surface). Max 50 characters. Blank and Null are allowed.', max_length=50, null=True)),
                ('price', models.CharField(help_text='TV price (surface). Max 10 characters.', max_length=10)),
                ('img', models.ImageField(blank=True, null=True, upload_to='tv_surface/')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, help_text='Created', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Updated', verbose_name='Updated')),
                ('order', models.PositiveIntegerField(blank=True, default=0, help_text='Orden de visualización', null=True, verbose_name='Orden')),
            ],
            options={
                'verbose_name': 'TV Surface',
                'verbose_name_plural': 'TV Surface',
                'db_table': 'apps_tv_surface',
                'ordering': ['order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='TVWallMountModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='TV title (wall-mount). Max 25 characters. Blank and Null are allowed.', max_length=25, null=True)),
                ('description', models.CharField(blank=True, help_text='TV description (wall-mount). Max 50 characters. Blank and Null are allowed.', max_length=50, null=True)),
                ('price', models.CharField(help_text='TV price (wall-mount). Max 10 characters.', max_length=10)),
                ('img', models.ImageField(blank=True, null=True, upload_to='tv_wall_mount/')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, help_text='Created', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Updated', verbose_name='Updated')),
                ('order', models.PositiveIntegerField(blank=True, default=0, help_text='Orden de visualización', null=True, verbose_name='Orden')),
            ],
            options={
                'verbose_name': 'TV Wall Mount',
                'verbose_name_plural': 'TV Wall Mount',
                'db_table': 'apps_tv_wall_mount',
                'ordering': ['order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='TVWallMountInstallationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('helpTechnician', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], help_text='Help technician. Max 1 character. choices: Y or N.', max_length=1)),
                ('takeDownTV', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], help_text='Take down TV. Max 1 character. choices: Y or N.', max_length=1)),
                ('comments', models.TextField(blank=True, help_text='Comments. Blank and Null are allowed.', null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, help_text='Created', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Updated', verbose_name='Updated')),
                ('order', models.PositiveIntegerField(blank=True, default=0, help_text='Orden de visualización', null=True, verbose_name='Orden')),
                ('TVHandleCords', models.ForeignKey(help_text='TV handle cords. Required. Foreign Key to TVHandleCordsModel.', on_delete=django.db.models.deletion.CASCADE, to='dynamicform.tvhandlecordsmodel')),
                ('TVOtherInstalations', models.ForeignKey(help_text='TV other instalations. Required. Foreign Key to TVOtherInstallsModel.', on_delete=django.db.models.deletion.CASCADE, to='dynamicform.tvotherinstallsmodel')),
                ('TVWallMount', models.ForeignKey(help_text='TV wall mount. Required. Foreign Key to TVWallMountModel.', on_delete=django.db.models.deletion.CASCADE, to='dynamicform.tvwallmountmodel')),
                ('TVsize', models.ForeignKey(help_text='TV size. Required. Foreign Key to TVSizeModel.', on_delete=django.db.models.deletion.CASCADE, to='dynamicform.tvsizemodel')),
                ('TVsurface', models.ForeignKey(help_text='TV surface. Required. Foreign Key to TVSurfaceModel.', on_delete=django.db.models.deletion.CASCADE, to='dynamicform.tvsurfacemodel')),
                ('otherQuestions', models.ManyToManyField(blank=True, help_text='TV other questions.', to='dynamicform.tvquestionsmodel')),
            ],
            options={
                'verbose_name': 'Form TV Model',
                'verbose_name_plural': 'Form TV Model',
                'db_table': 'apps_tv_wall_mount_installation',
                'ordering': ['order', 'id'],
            },
        ),
    ]

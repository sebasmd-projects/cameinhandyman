from django.utils import timezone

from django.db import models


class ContactInfoModel(models.Model):
    email = models.EmailField(
        'Email',
        help_text='Email',
        max_length=255
    )

    zipCode = models.CharField(
        'Zip Code',
        help_text='Zip Code',
        max_length=12,
        blank=True,
        null=True
    )

    state = models.CharField(
        'State',
        help_text='State',
        max_length=100,
        blank=True,
        null=True
    )

    celPhone = models.CharField(
        'Cellphone',
        max_length=30,
        help_text='Cellphone',
    )

    created = models.DateTimeField(
        'Created',
        default=timezone.now,
        help_text="Created",
    )

    updated = models.DateTimeField(
        'Updated',
        auto_now=True,
        help_text="Updated",
    )

    order = models.PositiveIntegerField(
        'Orden',
        default=0,
        help_text="Orden de visualización",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.email} - {self.celPhone} - {self.zipCode} - {self.state}"
    
    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"
        db_table = "apps_contactinfo"
        ordering = ['order', 'id']
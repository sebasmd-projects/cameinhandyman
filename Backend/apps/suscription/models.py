from django.utils import timezone
from django.db import models

class SuscriptionModel(models.Model):
    email = models.EmailField(
        max_length=200
    )
    
    created = models.DateTimeField(
        'Fecha de cración',
        default=timezone.now,
        help_text="Fecha de creación del usuario",
    )

    updated = models.DateTimeField(
        'Fecha de edición',
        auto_now=True,
        help_text="Fecha de edición del usuario",
    )

    order = models.PositiveIntegerField(
        'Orden',
        default=0,
        help_text="Orden de visualización",
        blank=True, null=True,
    )
    
    def __str__(self):
        return f"{self.id} - {self.email}"
    
    class Meta:
        verbose_name = "Suscription"
        verbose_name_plural = "Suscription"
        db_table = "apps_suscription"
        ordering = ['order', 'id']
